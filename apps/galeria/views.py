from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForms

def index(request):
    """
    Renderiza o template 'index.html' e retorna o HTML renderizado como resposta.

    Parâmetros:
        request (HttpRequest): O objeto de requisição HTTP.

    Retorna:
        HttpResponse: O HTML renderizado como resposta.
    """
    if not request.user.is_authenticated:
        messages.error(request, 'Usuario não logado!')
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True)
    return render(request, '../templates/galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    """
    Renderiza o modelo 'imagem.html' e retorna o HTML renderizado como resposta.

    Parâmetros:
        request (HttpRequest): O objeto de requisição HTTP.

    Retorna:
        HttpResponse: A resposta HTML renderizada.
    """
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, '../templates/galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    """
    Função para buscar fotografias com base em um parâmetro de consulta fornecido.
    
    Parâmetros:
    - request: objeto HttpRequest contendo os parâmetros de consulta
    
    Retorna:
    - Modelo renderizado com uma lista de fotografias com base na consulta de busca
    """
    if not request.user.is_authenticated:
        messages.error(request, 'Usuario não logado!')
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, 'galeria/index.html', {"cards": fotografias})

def nova_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuario não logado!')
        return redirect('login')

    form = FotografiaForms

    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nova fotografia cadastrada com sucesso!')
            return redirect('index')

    return render(request, 'galeria/nova_imagem.html', {"form": form})

def editar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    form = FotografiaForms(instance=fotografia)

    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fotografia editada com sucesso!')
            return redirect('index')

    return render(request, 'galeria/editar_imagem.html', {'form': form, 'foto_id': foto_id})

def deletar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request, 'Fotografia excluída com sucesso!')
    return redirect('index')

def filtro(request, categoria):
    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True, categoria=categoria)

    return render(request, 'galeria/index.html', {"cards": fotografias})