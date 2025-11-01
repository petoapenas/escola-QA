from django.urls import path
from . import views

urlpatterns = [
path('', views.listar_alunos, name='aluno_listar'),
path('cadastrar/', views.cadastrar_aluno,
name='aluno_cadastrar'),
]