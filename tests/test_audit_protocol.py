"""El wrapper no convierte salida desconocida o diez hallazgos en verde."""
import os
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class AuditProtocolTests(unittest.TestCase):
    def audit(self, output, full=False, returncode=0):
        with tempfile.TemporaryDirectory() as tmp:
            directory=Path(tmp)
            (directory/'cli').mkdir()
            fake=directory/'node'
            fake.write_text('#!/bin/sh\ncat <<\'END_REPORT\'\n'+output+'\nEND_REPORT\nexit '+str(returncode)+'\n')
            fake.chmod(0o755)
            env=os.environ.copy()
            env.update(NODE=str(fake),IMPECCABLE_REPO=tmp,HTML_VALIDATE='/nonexistent/html-validate',PA11Y='/nonexistent/pa11y')
            script='audit-adri-full.sh' if full else 'audit-adri.sh'
            return subprocess.run([str(ROOT/'scripts'/script),str(ROOT/'tests/fixtures/contracts/valid-bold-signal.html')],env=env,capture_output=True,text=True)

    def test_diez_hallazgos_no_se_confunden_con_cero(self):
        result=self.audit('10 anti-patterns found\n  line 1: [gratuitous-decoration] example')
        self.assertEqual(result.returncode,1,result.stdout)

    def test_impeccable_exit_dos_significa_hallazgos(self):
        result=self.audit('  line 35: [overused-font] Google Fonts: Inter\n1 anti-pattern found.',returncode=2)
        self.assertEqual(result.returncode,0,result.stdout)

    def test_salida_desconocida_es_infraestructura(self):
        self.assertEqual(self.audit('Unexpected new CLI protocol').returncode,2)

    def test_silencio_con_exit_cero_es_conforme(self):
        self.assertEqual(self.audit('').returncode,0)
        self.assertEqual(self.audit('',returncode=2).returncode,2)

    def test_cero_hallazgos_es_conforme(self):
        self.assertEqual(self.audit('0 anti-patterns found').returncode,0)

    def test_auditoria_full_sin_binarios_no_instala(self):
        result=self.audit('0 anti-patterns found',full=True)
        self.assertEqual(result.returncode,2,result.stdout)
        self.assertIn('faltan html-validate o pa11y instalados',result.stdout)


if __name__=='__main__':unittest.main()
