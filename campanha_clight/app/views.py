from django.shortcuts import render

# Create your views here.

def compartilhe(request, palavra):
    textos = __getType(palavra)

    context = {
    'cor': textos['cor'],
    'palavra': textos['palavra'],
    'class': textos['class'],
    }
    return render(request,
                  'app/compartilhe.html',
                  context=context)

def cor(request, palavra):
    textos = __getType(palavra)

    context = {
    'cor': textos['cor'],
    'palavra': textos['palavra'],
    'class': textos['class'],
    }
    return render(request,
                  'app/cor.html',
                  context=context)


def __getType(palavra):

    if(palavra == "romantica"):
        mpalavra = "ROMÂNTICA"
        cor = "ROSA"
        mclass="romantica"
    elif(palavra == "livre"):
        mpalavra = "LIVRE"
        cor = "ROSA"
        mclass="livre"
    elif(palavra == "poderosa"):
        mpalavra = "PODEROSA"
        cor = "ROSA"
        mclass="poderosa"
    elif(palavra == "descolada"):
        mpalavra = "DESCOLADA"
        cor = "LARANJA"
        mclass="descolada"
    elif(palavra == "forte"):
        mpalavra = "FORTE"
        cor = "LARANJA"
        mclass="forte"
    elif(palavra == "alegre"):
        mpalavra = "ALEGRE"
        cor = "LARANJA"
        mclass="alegre"
    elif(palavra == "feliz"):
        mpalavra = "FELIZ"
        cor = "VERDE"
        mclass="feliz"
    elif(palavra == "inspiradora"):
        mpalavra = "INSPIRADORA"
        cor = "VERDE"
        mclass="inspiradora"
    elif(palavra == "otimista"):
        mpalavra = "OTIMISTA"
        cor = "VERDE"
        mclass="otimista"
    elif(palavra == "sincera"):
        mpalavra = "SINCERA"
        cor = "AZUL"
        mclass="sincera"
    elif(palavra == "tranquila"):
        mpalavra = "TRANQUILA"
        cor = "AZUL"
        mclass="tranquila"
    else:
        mpalavra = "CONFIANTE"
        cor = "AZUL"
        mclass="confiante"

    textos = {
        'cor': cor,
        'palavra': mpalavra,
        'class': mclass,
    }

    return textos

