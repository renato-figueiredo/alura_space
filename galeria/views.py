from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia

def index(request):
    """
    Renderiza o template 'index.html' e retorna o HTML renderizado como resposta.

    Parâmetros:
        request (HttpRequest): O objeto de requisição HTTP.

    Retorna:
        HttpResponse: O HTML renderizado como resposta.
    """
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
    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, '../templates/galeria/buscar.html', {"cards": fotografias})