from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

from usuarios.forms import LoginForms, CadastroForms


def login(request):
    """
    Renderiza a página de login e lida com a funcionalidade de login.

    Parâmetros:
        request (HttpRequest): O objeto de requisição HTTP.

    Retorna:
        HttpResponse: O objeto de resposta HTTP.

    """
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()

        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
        )
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f'Login {nome} realizado com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Login ou senha inválidos!')
            return redirect('login')

    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    """
    Uma função que lida com o cadastro de usuários. Ela recebe um objeto de requisição como parâmetro e retorna uma página HTML renderizada para o cadastro de usuários com um formulário.
    """
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)
        
        if form.is_valid():
            if form['senha_1'].value() != form['senha_2'].value():
                messages.error(request, 'As senhas precisam ser iguais!')
                return redirect('cadastro')
            
            nome=form['nome_cadastro'].value()
            email=form['email'].value()
            senha=form['senha_1'].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Usuário já existe!')
                return redirect('cadastro')
            
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, 'Cadastrado com sucesso!')
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {'form': form})

def logout(request):
    """
    Efetua o logout do usuário chamando a função `logout` do módulo `auth`.

    Parâmetros:
        request (HttpRequest): O objeto de requisição HTTP representando a requisição atual.

    Retorna:
        HttpResponseRedirect: Uma resposta de redirecionamento para a URL 'index'.
    """
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('login')