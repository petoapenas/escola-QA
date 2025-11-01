from django.shortcuts import render, redirect
from .models import Aluno
from .forms import AlunoForm

def listar_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos/listar.html', {'alunos': alunos})

def cadastrar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
    
        if form.is_valid():
            form.save()
            return redirect('aluno_listar')

    else:
        form = AlunoForm()
    return render(request, 'alunos/cadastrar.html', {'form': form})