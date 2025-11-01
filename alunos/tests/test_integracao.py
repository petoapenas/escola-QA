from django.test import TestCase
from django.urls import reverse
from alunos.models import Aluno


class AlunoIntegracaoTest(TestCase):
    def test_criar_e_listar_aluno(self):
# Cria via model
        Aluno.objects.create(nome="Paulo", idade=19)
        resposta = self.client.get(reverse('aluno_listar'))
        self.assertContains(resposta, "Paulo")
        
    def test_criar_aluno_via_post(self):
        resposta = self.client.post(reverse('aluno_cadastrar'),
{"nome": "Lúcia", "idade": 21})
        self.assertEqual(resposta.status_code, 302) # Redireciona
        self.assertTrue(Aluno.objects.filter(nome="Lúcia").exists())