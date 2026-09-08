// Node 22+ y Chrome instalados; servidor local y protocolo DevTools, sin npm.
import {spawn} from 'node:child_process';
import {createServer} from 'node:http';
import {readFile, mkdtemp, rm, access} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {join, resolve, extname} from 'node:path';
import {fileURLToPath} from 'node:url';

const root = resolve(fileURLToPath(new URL('..', import.meta.url)));
const chrome = process.env.CHROME_BIN || (process.platform === 'darwin' ? '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' : '/usr/bin/google-chrome');
const prefix = process.env.BROWSER_FIXTURE_PREFIX || '';
const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));
let browser, socket, profile, server;
let sequence = 0;
const pending = new Map();
function command(method, params = {}) {
  const id = ++sequence;
  return new Promise((resolve, reject) => {
    const timer = setTimeout(() => { pending.delete(id); reject(new Error(`Timeout: ${method}`)); }, 30000);
    pending.set(id, {resolve, reject, timer});
    socket.send(JSON.stringify({id, method, params}));
  });
}
async function evaluate(expression) {
  const result = await command('Runtime.evaluate', {expression, awaitPromise:true, returnByValue:true});
  if (result.exceptionDetails) throw new Error(JSON.stringify(result.exceptionDetails));
  return result.result.value;
}
try {
  await access(chrome);
  profile = await mkdtemp(join(tmpdir(), 'adri-style-browser-'));
  server = createServer(async (req, res) => {
    try {
      const path = resolve(root, '.' + decodeURIComponent(new URL(req.url,'http://localhost').pathname));
      if (!path.startsWith(root + '/')) { res.writeHead(403).end(); return; }
      const mime = {'.html':'text/html', '.css':'text/css', '.js':'text/javascript', '.json':'application/json'};
      res.setHeader('Content-Type', (mime[extname(path)] || 'application/octet-stream') + '; charset=utf-8');
      res.end(await readFile(path));
    } catch { res.writeHead(404).end(); }
  });
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  browser = spawn(chrome, ['--headless=new', '--disable-gpu', '--no-first-run', '--no-default-browser-check',
    '--remote-debugging-port=0', `--user-data-dir=${profile}`, ...(process.platform === 'linux' ? ['--no-sandbox'] : []), 'about:blank'], {stdio:'ignore'});
  browser.on('error', error => { console.error(error.message); process.exitCode=2; });
  let port;
  for (let i=0;i<100;i++) {
    try { port=(await readFile(join(profile,'DevToolsActivePort'),'utf8')).split('\n')[0]; break; } catch { await sleep(100); }
  }
  if (!port) throw new Error('Chrome no publicó DevToolsActivePort');
  const target = await (await fetch(`http://127.0.0.1:${port}/json/new?about:blank`,{method:'PUT'})).json();
  socket = new WebSocket(target.webSocketDebuggerUrl);
  await new Promise((resolve,reject) => { socket.onopen=resolve; socket.onerror=reject; });
  socket.onmessage = event => {
    const data = JSON.parse(event.data), task = pending.get(data.id);
    if (!task) return;
    clearTimeout(task.timer); pending.delete(data.id);
    if (data.error) task.reject(new Error(JSON.stringify(data.error))); else task.resolve(data.result);
  };
  await command('Page.enable');
  const checks = await readFile(join(root,'tests/browser-checks.js'),'utf8');
  const paths = ['assets/preset-catalog.html','templates/bootstrap-adri.html','templates/adri-console.html',
    ...['console','gallery','dashboard','presentation'].map(name=>`tests/fixtures/surfaces/${name}.html`)];
  let assertions = 0;
  const failures = [];
  for (const [width,height] of [[1440,1000],[768,1024],[375,812],[320,568]]) {
    await command('Emulation.setDeviceMetricsOverride',{width,height,deviceScaleFactor:1,mobile:false});
    for (const path of paths) {
      await command('Page.navigate',{url:`http://127.0.0.1:${server.address().port}/${prefix}${path}`});
      let ready = false;
      for (let i=0;i<150;i++) {
        if (await evaluate(`document.readyState === "complete" && location.pathname === ${JSON.stringify('/'+prefix+path)}`)) { ready = true; break; }
        await sleep(100);
      }
      if (!ready) throw new Error(`Carga incompleta: ${path}`);
      const result = await evaluate(checks+'\nbrowserChecks()');
      assertions += result.assertions;
      failures.push(...result.failures.map(message=>`${width}×${height} ${path}: ${message}`));
      await command('Emulation.setEmulatedMedia',{media:'print'});
      const printed = await evaluate(`({bg:getComputedStyle(document.body).backgroundColor,overflow:document.documentElement.scrollWidth>innerWidth+2})`);
      assertions++;
      if (printed.overflow) failures.push(`${path}: desbordamiento en impresión`);
      assertions++;
      if (printed.bg !== 'rgb(255, 255, 255)') failures.push(`${path}: impresión sin fondo blanco`);
      await command('Emulation.setEmulatedMedia',{media:'',features:[{name:'prefers-reduced-motion',value:'reduce'}]});
      assertions++;
      if (!await evaluate('matchMedia("(prefers-reduced-motion: reduce)").matches')) failures.push('No se emuló movimiento reducido');
    }
  }
  console.log(JSON.stringify({assertions,failures},null,2));
  process.exitCode = failures.length ? 1 : 0;
} catch (error) {
  console.error(`BROWSER_INFRASTRUCTURE_ERROR: ${error.message}`); process.exitCode = 2;
} finally {
  if (socket) socket.close();
  if (browser && browser.exitCode === null) {
    browser.kill('SIGTERM');
    await new Promise(resolve=>{ browser.once('exit',resolve); setTimeout(resolve,3000); });
  }
  if (server) await new Promise(resolve=>server.close(resolve));
  if (profile) await rm(profile,{recursive:true,force:true,maxRetries:3,retryDelay:200});
}
