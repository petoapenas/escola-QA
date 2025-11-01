from django.test import SimpleTestCase
from django.urls import reverse, resolve
from alunos.views import listar_alunos, cadastrar_aluno
class UrlsTest(SimpleTestCase):

    def test_url_lista_resolve_view(self):
        url = reverse('aluno_listar')
        self.assertEqual(resolve(url).func, listar_alunos)
    def test_url_cadastrar_resolve_view(self):
        url = reverse('aluno_cadastrar')
        self.assertEqual(resolve(url).func, cadastrar_aluno)