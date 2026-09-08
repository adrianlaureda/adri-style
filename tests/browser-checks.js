// Pruebas DOM reales: se ejecutan en Chrome, sin bibliotecas externas.
async function browserChecks() {
  const failures = [];
  let assertions = 0;
  const check = (condition, message) => { assertions++; if (!condition) failures.push(message); };
  const style = (selector) => getComputedStyle(document.querySelector(selector));
  const fits = (el) => el.scrollWidth <= el.clientWidth + 2;
  check(fits(document.documentElement), 'La página desborda horizontalmente');
  if (document.querySelector('#preset-data')) {
    const presets = JSON.parse(document.querySelector('#preset-data').textContent);
    for (const preset of presets) {
      document.querySelector(`[data-preset-id="${preset.id}"]`).click();
      check(document.querySelector('#preview').dataset.preset === preset.id, `${preset.id}: marca de preview`);
      check(style('#preview-name').fontWeight === String(preset.preview?.display_weight), `${preset.id}: peso display`);
      check([...document.querySelectorAll('link[rel="stylesheet"]')].some(link => link.dataset.presetFont !== undefined), `${preset.id}: carga de fuentes`);
      check((style('#preview').backgroundImage !== 'none') === Boolean(preset.color.background_image), `${preset.id}: fondo contextual`);
      if (preset.fonts.local_stylesheet) {
        for (let attempt=0;attempt<100 && document.querySelector('#font-status').textContent === 'Cargando tipografías…';attempt++) await new Promise(resolve=>setTimeout(resolve,50));
        const faces = await document.fonts.load('500 16px "Barlow"');
        check(faces.length > 0, `${preset.id}: Barlow local disponible`);
      }
      for (const name of ['console', 'gallery', 'dashboard', 'presentation']) {
        document.querySelector(`[data-surface-option="${name}"]`).click();
        const surface = document.querySelector(`.surface[data-surface="${name}"]`);
        check([...document.querySelectorAll('.surface')].filter(el => getComputedStyle(el).display !== 'none').length === 1, `${name}: única superficie visible`);
        if (name !== 'dashboard') check(getComputedStyle(surface).display === 'grid', `${name}: conserva grid`);
        check(fits(surface), `${preset.id}/${name}: contenido recortado`);
        check(fits(document.documentElement), `${preset.id}/${name}: viewport desbordado`);
      }
    }
    for (const preset of presets.slice(0,4)) {
      document.querySelector(`[data-preset-id="${preset.id}"]`).click();
      document.querySelector('#compare-action').click();
    }
    check(document.querySelectorAll('.compare-card').length === 3, 'Comparación limitada a tres');
    document.querySelector('#compare-action').click();
    check(document.querySelectorAll('.compare-card').length === 2, 'Quitar comparación');
    document.querySelector('[data-preset-id="01-bold-signal"]').click();
    document.querySelector('[data-surface-option="console"]').click();
  }
  if (document.querySelector('[data-action="toggle-theme"]')) {
    const button = document.querySelector('[data-action="toggle-theme"]');
    for (const theme of ['dark', 'light']) {
      if (document.documentElement.dataset.theme !== theme) button.click();
      check(document.documentElement.dataset.theme === theme, `Toggle ${theme}`);
      check(button.getAttribute('aria-label') === (theme === 'dark' ? 'Activar modo claro' : 'Activar modo oscuro'), `Label ${theme}`);
      check(style(theme === 'dark' ? '.icon-sun' : '.icon-moon').display !== 'none', `Icono ${theme}`);
      check(style('html').colorScheme === theme, `color-scheme ${theme}`);
      check(fits(document.documentElement), `Bootstrap ${theme}: ancho`);
    }
  }
  if (document.documentElement.dataset.preset === '28-adri-console') {
    const toggle = document.querySelector('.theme-toggle');
    for (const theme of ['light','dark']) {
      if (document.documentElement.dataset.theme !== theme) toggle.click();
      check(document.documentElement.dataset.theme === theme, `Console: tema ${theme}`);
      check(style(theme === 'dark' ? '.icon-moon' : '.icon-sun').display !== 'none', `Console: icono ${theme}`);
      check(style('body').backgroundImage.includes('gradient'), `Console: gradiente ${theme}`);
      check(fits(document.documentElement), `Console: ancho ${theme}`);
    }
    check((await document.fonts.load('500 16px "Barlow"')).length > 0, 'Console: fuente local');
  }
  if (document.querySelector('body > .slide-count')) {
    check(document.querySelector('.slide-stage').scrollHeight <= innerHeight + 2, 'Presentación recortada en altura');
  }
  return {assertions,failures,viewport:[innerWidth,innerHeight]};
}
