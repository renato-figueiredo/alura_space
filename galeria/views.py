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