from django.shortcuts import render

def index(request):
    """
    Renderiza o template 'index.html' e retorna o HTML renderizado como resposta.

    Parâmetros:
        request (HttpRequest): O objeto de requisição HTTP.

    Retorna:
        HttpResponse: O HTML renderizado como resposta.
    """

    dados = {
        1: {
            "nome": "Nebula de Carina",
            "legenda": "webbtelescope.org / NASA / James Webb",
        },
        2: {
            "nome": "Galáxia NGC 3324",
            "legenda": "nasa.org / NASA / Hubble",
        }
    }

    return render(request, '../templates/galeria/index.html', {"cards": dados})

def imagem(request):
    """
    Renderiza o modelo 'imagem.html' e retorna o HTML renderizado como resposta.

    Parâmetros:
        request (HttpRequest): O objeto de requisição HTTP.

    Retorna:
        HttpResponse: A resposta HTML renderizada.
    """
    return render(request, '../templates/galeria/imagem.html')