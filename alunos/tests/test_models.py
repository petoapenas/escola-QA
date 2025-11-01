from django.test import TestCase
from alunos.models import Aluno


class AlunoModelTest(TestCase):
    def test_str_retorna_nome(self):

        aluno = Aluno.objects.create(nome="Maria", idade=18)
        self.assertEqual(str(aluno), "Maria")