from django.shortcuts import render
from galeria.models import Fotografia

def index(request):
    """
    Renderiza o template 'index.html' e retorna o HTML renderizado como resposta.

    Parâmetros:
        request (HttpRequest): O objeto de requisição HTTP.

    Retorna:
        HttpResponse: O HTML renderizado como resposta.
    """
    fotografias = Fotografia.objects.all()
    return render(request, '../templates/galeria/index.html', {"cards": fotografias})

def imagem(request):
    """
    Renderiza o modelo 'imagem.html' e retorna o HTML renderizado como resposta.

    Parâmetros:
        request (HttpRequest): O objeto de requisição HTTP.

    Retorna:
        HttpResponse: A resposta HTML renderizada.
    """
    return render(request, '../templates/galeria/imagem.html')