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

    if palavra == "impulsiva":
        mpalavra = "IMPULSIVA"
        cor = "VERMELHO"
        mclass = "impulsiva"
        image = "app/imagens/produto-uva.png"
        produto = "UVA"
        slogan = "O LADO IMPULSIVO DE CLIGHT."
        texto= "<p>De rosa, você está feliz. E mais do que isso, está também romântica.</p><p>Hoje você deve explorar esse seu lado para deixar a vida mais leve, fazendo só o que vai arrancar lindos sorrisos. E, se tiver alguém, aproveite para viver momentos à dois, com tudo que você tem direito.<p>Curta esse momento com toda a leveza. Espalhe amor por onde for.</p><p>Até porque o amor deixa todo mundo feliz.</p>"


    elif palavra == "linda":
        mpalavra = "LINDA"
        cor = "ROSA"
        mclass = "linda"
        image = "app/imagens/produto-uva.png"
        produto = "UVA"
        slogan = "O LADO LINDO DE CLIGHT."
        texto= "<p>2De rosa, você está feliz. E mais do que isso, está também romântica.</p><p>Hoje você deve explorar esse seu lado para deixar a vida mais leve, fazendo só o que vai arrancar lindos sorrisos. E, se tiver alguém, aproveite para viver momentos à dois, com tudo que você tem direito.<p>Curta esse momento com toda a leveza. Espalhe amor por onde for.</p><p>Até porque o amor deixa todo mundo feliz.</p>"

    elif palavra == "extrovertida":
        mpalavra = "EXTROVERTIDA"
        cor = "AMARELO"
        mclass = "extrovertida"
        image = "app/imagens/produto-uva.png"
        produto = "UVA"
        slogan = "O LADO EXTROVERTIDO DE CLIGHT."
        texto= "<p>2De rosa, você está feliz. E mais do que isso, está também romântica.</p><p>Hoje você deve explorar esse seu lado para deixar a vida mais leve, fazendo só o que vai arrancar lindos sorrisos. E, se tiver alguém, aproveite para viver momentos à dois, com tudo que você tem direito.<p>Curta esse momento com toda a leveza. Espalhe amor por onde for.</p><p>Até porque o amor deixa todo mundo feliz.</p>"


    elif palavra == "vaidosa":
        mpalavra = "VAIDOSA"
        cor = "PINK"
        mclass = "vaidosa"
        image = "app/imagens/produto-tangerina.png"
        produto = "TANGERINA"
        slogan = "O LADO VAIDOSO DE CLIGHT."
        texto= "<p>2De rosa, você está feliz. E mais do que isso, está também romântica.</p><p>Hoje você deve explorar esse seu lado para deixar a vida mais leve, fazendo só o que vai arrancar lindos sorrisos. E, se tiver alguém, aproveite para viver momentos à dois, com tudo que você tem direito.<p>Curta esse momento com toda a leveza. Espalhe amor por onde for.</p><p>Até porque o amor deixa todo mundo feliz.</p>"

    elif palavra == "confiante":
        mpalavra = "CONFIANTE"
        cor = "BORDÔ"
        mclass = "confiante"
        image = "app/imagens/produto-tangerina.png"
        produto = "TANGERINA"
        slogan = "O LADO CONFIANTE DE CLIGHT."
        texto= "<p>2De rosa, você está feliz. E mais do que isso, está também romântica.</p><p>Hoje você deve explorar esse seu lado para deixar a vida mais leve, fazendo só o que vai arrancar lindos sorrisos. E, se tiver alguém, aproveite para viver momentos à dois, com tudo que você tem direito.<p>Curta esse momento com toda a leveza. Espalhe amor por onde for.</p><p>Até porque o amor deixa todo mundo feliz.</p>"

    elif palavra == "fitness":
        mpalavra = "FITNESS"
        cor = "VERDE"
        mclass = "fitness"
        image = "app/imagens/produto-tangerina.png"
        produto = "TANGERINA"
        slogan = "O LADO FITNESS DE CLIGHT."
        texto= "<p>2De rosa, você está feliz. E mais do que isso, está também romântica.</p><p>Hoje você deve explorar esse seu lado para deixar a vida mais leve, fazendo só o que vai arrancar lindos sorrisos. E, se tiver alguém, aproveite para viver momentos à dois, com tudo que você tem direito.<p>Curta esse momento com toda a leveza. Espalhe amor por onde for.</p><p>Até porque o amor deixa todo mundo feliz.</p>"

    elif palavra == "livre":
        mpalavra = "LIVRE"
        cor = "TURQUESA"
        mclass = "livre"
        image = "app/imagens/produto-morango.png"
        produto = "MORANGO"
        slogan = "O LADO LIVRE DE CLIGHT."
        texto= "<p>2De rosa, você está feliz. E mais do que isso, está também romântica.</p><p>Hoje você deve explorar esse seu lado para deixar a vida mais leve, fazendo só o que vai arrancar lindos sorrisos. E, se tiver alguém, aproveite para viver momentos à dois, com tudo que você tem direito.<p>Curta esse momento com toda a leveza. Espalhe amor por onde for.</p><p>Até porque o amor deixa todo mundo feliz.</p>"

    elif palavra == "misteriosa":
        mpalavra = "MISTERIOSA"
        cor = "VIOLETA"
        mclass = "misteriosa"
        image = "app/imagens/produto-morango.png"
        produto = "MORANGO"
        slogan = "O LADO MISTERIOSO DE CLIGHT."
        texto= "<p>2De rosa, você está feliz. E mais do que isso, está também romântica.</p><p>Hoje você deve explorar esse seu lado para deixar a vida mais leve, fazendo só o que vai arrancar lindos sorrisos. E, se tiver alguém, aproveite para viver momentos à dois, com tudo que você tem direito.<p>Curta esse momento com toda a leveza. Espalhe amor por onde for.</p><p>Até porque o amor deixa todo mundo feliz.</p>"

    elif palavra == "otimista":
        mpalavra = "OTIMISTA"
        cor = "LARANJA"
        mclass = "otimista"
        image = "app/imagens/produto-morango.png"
        produto = "MORANGO"
        slogan = "O LADO OTIMISTA DE CLIGHT."
        texto= "<p>2De rosa, você está feliz. E mais do que isso, está também romântica.</p><p>Hoje você deve explorar esse seu lado para deixar a vida mais leve, fazendo só o que vai arrancar lindos sorrisos. E, se tiver alguém, aproveite para viver momentos à dois, com tudo que você tem direito.<p>Curta esse momento com toda a leveza. Espalhe amor por onde for.</p><p>Até porque o amor deixa todo mundo feliz.</p>"

    elif palavra == "poderosa":
        mpalavra = "PODEROSA"
        cor = "AZUL MARINHO"
        mclass = "poderosa"
        image = "app/imagens/produto-maracuja.png"
        produto = "MARACUJÁ"
        slogan = "O LADO PODEROSO DE CLIGHT."
        texto= "<p>2De rosa, você está feliz. E mais do que isso, está também romântica.</p><p>Hoje você deve explorar esse seu lado para deixar a vida mais leve, fazendo só o que vai arrancar lindos sorrisos. E, se tiver alguém, aproveite para viver momentos à dois, com tudo que você tem direito.<p>Curta esse momento com toda a leveza. Espalhe amor por onde for.</p><p>Até porque o amor deixa todo mundo feliz.</p>"

    elif palavra == "zen":
        mpalavra = "ZEN"
        cor = "AZUL"
        mclass = "zen"
        image = "app/imagens/produto-maracuja.png"
        produto = "MARACUJÁ"
        slogan = "O LADO ZEN DE CLIGHT."
        texto= "<p>2De rosa, você está feliz. E mais do que isso, está também romântica.</p><p>Hoje você deve explorar esse seu lado para deixar a vida mais leve, fazendo só o que vai arrancar lindos sorrisos. E, se tiver alguém, aproveite para viver momentos à dois, com tudo que você tem direito.<p>Curta esse momento com toda a leveza. Espalhe amor por onde for.</p><p>Até porque o amor deixa todo mundo feliz.</p>"

    elif palavra == "apaixonada":
        mpalavra = "APAIXONADA"
        cor = "LILÁS"
        mclass = "apaixonada"
        image = "app/imagens/produto-maracuja.png"
        produto = "MARACUJÁ"
        slogan = "O LADO APAIXONADO DE CLIGHT."
        texto= "<p>2De rosa, você está feliz. E mais do que isso, está também romântica.</p><p>Hoje você deve explorar esse seu lado para deixar a vida mais leve, fazendo só o que vai arrancar lindos sorrisos. E, se tiver alguém, aproveite para viver momentos à dois, com tudo que você tem direito.<p>Curta esse momento com toda a leveza. Espalhe amor por onde for.</p><p>Até porque o amor deixa todo mundo feliz.</p>"

    else:
        raise Http404("Page not Found")

    context = {
        'cor': cor,
        'palavra': mpalavra,
        'class': mclass,
        'image': image,
        'produto': produto,
        'slogan': slogan,
        'texto': texto
    }

    return context
