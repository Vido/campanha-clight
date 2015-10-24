from django.http import Http404
from django.shortcuts import render

# Create your views here.

def compartilhe(request, palavra):
    context = __getType(palavra)
    return render(request,
                  'app/compartilhe.html',
                  context=context)

def cor(request, palavra):
    context = __getType(palavra)
    return render(request,
                  'app/cor.html',
                  context=context)

def sabor(request, palavra):
    context = __getType(palavra)
    return render(request,
                  'app/sabor.html',
                  context=context)

def __getType(palavra):

    if palavra == "romantica":
        mpalavra = "ROMÂNTICA"
        cor = "ROSA"
        mclass = "romantica"
        image = "app/imagens/produto-1.png"

    elif palavra == "livre":
        mpalavra = "LIVRE"
        cor = "ROSA"
        mclass = "livre"

    elif palavra == "poderosa":
        mpalavra = "PODEROSA"
        cor = "ROSA"
        mclass = "poderosa"
        image = "app/imagens/produto-1.png"

    elif palavra == "descolada":
        mpalavra = "DESCOLADA"
        cor = "LARANJA"
        mclass = "descolada"
        image = "app/imagens/produto-1.png"

    elif palavra == "forte":
        mpalavra = "FORTE"
        cor = "LARANJA"
        mclass = "forte"
        image = "app/imagens/produto-1.png"

    elif palavra == "alegre":
        mpalavra = "ALEGRE"
        cor = "LARANJA"
        mclass = "alegre"
        image = "app/imagens/produto-1.png"

    elif palavra == "feliz":
        mpalavra = "FELIZ"
        cor = "VERDE"
        mclass = "feliz"
        image = "app/imagens/produto-1.png"

    elif palavra == "inspiradora":
        mpalavra = "INSPIRADORA"
        cor = "VERDE"
        mclass = "inspiradora"
        image = "app/imagens/produto-1.png"

    elif palavra == "otimista":
        mpalavra = "OTIMISTA"
        cor = "VERDE"
        mclass = "otimista"
        image = "app/imagens/produto-1.png"

    elif palavra == "sincera":
        mpalavra = "SINCERA"
        cor = "AZUL"
        mclass = "sincera"
        image = "app/imagens/produto-1.png"

    elif palavra == "tranquila":
        mpalavra = "TRANQUILA"
        cor = "AZUL"
        mclass = "tranquila"
        image = "app/imagens/produto-1.png"

    elif palavra == "confiante":
        mpalavra = "CONFIANTE"
        cor = "AZUL"
        mclass = "confiante"
        image = "app/imagens/produto-1.png"
    else:
        raise Http404("Page not Found")

    context = {
        'cor': cor,
        'palavra': mpalavra,
        'class': mclass,
        'image': image
    }

    return context
