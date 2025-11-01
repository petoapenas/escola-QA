from django.test import TestCase
from django.urls import reverse
from alunos.models import Aluno


class AlunoListViewTest(TestCase):
    def test_pagina_lista_carrega(self):
        url = reverse('aluno_listar')
        resposta = self.client.get(url)
        self.assertEqual(resposta.status_code, 200)
    def test_lista_exibe_aluno(self):
        Aluno.objects.create(nome="Carlos", idade=20)
        resposta = self.client.get(reverse('aluno_listar'))
        self.assertContains(resposta, "Carlos")