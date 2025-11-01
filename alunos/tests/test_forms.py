from django.test import TestCase
from alunos.forms import AlunoForm


class AlunoFormTest(TestCase):
    def test_form_valido(self):
        form = AlunoForm(data={"nome": "João", "idade": 22})
        self.assertTrue(form.is_valid())
        
    def test_form_invalido_sem_nome(self):
        form = AlunoForm(data={"nome": "", "idade": 22})
        self.assertFalse(form.is_valid())