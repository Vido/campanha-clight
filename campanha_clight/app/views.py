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
        image = "app/imagens/produto-uva.png"
        produto = "UVA"
        slogan = "O LADO ROMÂNTICO DE CLIGHT."
        texto= "<p>De rosa, você está feliz. E mais do que isso, está também romântica.</p><p>Hoje você deve explorar esse seu lado para deixar a vida mais leve, fazendo só o que vai arrancar lindos sorrisos. E, se tiver alguém, aproveite para viver momentos à dois, com tudo que você tem direito.<p>Curta esse momento com toda a leveza. Espalhe amor por onde for.</p><p>Até porque o amor deixa todo mundo feliz.</p>"


    elif palavra == "livre":
        mpalavra = "LIVRE"
        cor = "ROSA"
        mclass = "livre"
        image = "app/imagens/produto-uva.png"
        produto = "UVA"
        slogan = "O LADO ROMÂNTICO DE CLIGHT."
        texto= "<p>2De rosa, você está feliz. E mais do que isso, está também romântica.</p><p>Hoje você deve explorar esse seu lado para deixar a vida mais leve, fazendo só o que vai arrancar lindos sorrisos. E, se tiver alguém, aproveite para viver momentos à dois, com tudo que você tem direito.<p>Curta esse momento com toda a leveza. Espalhe amor por onde for.</p><p>Até porque o amor deixa todo mundo feliz.</p>"

    elif palavra == "poderosa":
        mpalavra = "PODEROSA"
        cor = "ROSA"
        mclass = "poderosa"
        image = "app/imagens/produto-uva.png"
        produto = "UVA"
        slogan = "O LADO ROMÂNTICO DE CLIGHT."
        texto= "<p>2De rosa, você está feliz. E mais do que isso, está também romântica.</p><p>Hoje você deve explorar esse seu lado para deixar a vida mais leve, fazendo só o que vai arrancar lindos sorrisos. E, se tiver alguém, aproveite para viver momentos à dois, com tudo que você tem direito.<p>Curta esse momento com toda a leveza. Espalhe amor por onde for.</p><p>Até porque o amor deixa todo mundo feliz.</p>"


    elif palavra == "descolada":
        mpalavra = "DESCOLADA"
        cor = "LARANJA"
        mclass = "descolada"
        image = "app/imagens/produto-tangerina.png"
        produto = "TANGERINA"
        slogan = "O LADO ROMÂNTICO DE CLIGHT."
        texto= "<p>2De rosa, você está feliz. E mais do que isso, está também romântica.</p><p>Hoje você deve explorar esse seu lado para deixar a vida mais leve, fazendo só o que vai arrancar lindos sorrisos. E, se tiver alguém, aproveite para viver momentos à dois, com tudo que você tem direito.<p>Curta esse momento com toda a leveza. Espalhe amor por onde for.</p><p>Até porque o amor deixa todo mundo feliz.</p>"

    elif palavra == "forte":
        mpalavra = "FORTE"
        cor = "LARANJA"
        mclass = "forte"
        image = "app/imagens/produto-tangerina.png"
        produto = "TANGERINA"
        slogan = "O LADO ROMÂNTICO DE CLIGHT."
        texto= "<p>2De rosa, você está feliz. E mais do que isso, está também romântica.</p><p>Hoje você deve explorar esse seu lado para deixar a vida mais leve, fazendo só o que vai arrancar lindos sorrisos. E, se tiver alguém, aproveite para viver momentos à dois, com tudo que você tem direito.<p>Curta esse momento com toda a leveza. Espalhe amor por onde for.</p><p>Até porque o amor deixa todo mundo feliz.</p>"

    elif palavra == "alegre":
        mpalavra = "ALEGRE"
        cor = "LARANJA"
        mclass = "alegre"
        image = "app/imagens/produto-tangerina.png"
        produto = "TANGERINA"
        slogan = "O LADO ROMÂNTICO DE CLIGHT."
        texto= "<p>2De rosa, você está feliz. E mais do que isso, está também romântica.</p><p>Hoje você deve explorar esse seu lado para deixar a vida mais leve, fazendo só o que vai arrancar lindos sorrisos. E, se tiver alguém, aproveite para viver momentos à dois, com tudo que você tem direito.<p>Curta esse momento com toda a leveza. Espalhe amor por onde for.</p><p>Até porque o amor deixa todo mundo feliz.</p>"

    elif palavra == "feliz":
        mpalavra = "FELIZ"
        cor = "TURQUESA"
        mclass = "feliz"
        image = "app/imagens/produto-morango.png"
        produto = "MORANGO"
        slogan = "O LADO ROMÂNTICO DE CLIGHT."
        texto= "<p>2De rosa, você está feliz. E mais do que isso, está também romântica.</p><p>Hoje você deve explorar esse seu lado para deixar a vida mais leve, fazendo só o que vai arrancar lindos sorrisos. E, se tiver alguém, aproveite para viver momentos à dois, com tudo que você tem direito.<p>Curta esse momento com toda a leveza. Espalhe amor por onde for.</p><p>Até porque o amor deixa todo mundo feliz.</p>"

    elif palavra == "inspiradora":
        mpalavra = "INSPIRADORA"
        cor = "TURQUESA"
        mclass = "inspiradora"
        image = "app/imagens/produto-morango.png"
        produto = "MORANGO"
        slogan = "O LADO ROMÂNTICO DE CLIGHT."
        texto= "<p>2De rosa, você está feliz. E mais do que isso, está também romântica.</p><p>Hoje você deve explorar esse seu lado para deixar a vida mais leve, fazendo só o que vai arrancar lindos sorrisos. E, se tiver alguém, aproveite para viver momentos à dois, com tudo que você tem direito.<p>Curta esse momento com toda a leveza. Espalhe amor por onde for.</p><p>Até porque o amor deixa todo mundo feliz.</p>"

    elif palavra == "otimista":
        mpalavra = "OTIMISTA"
        cor = "TURQUESA"
        mclass = "otimista"
        image = "app/imagens/produto-morango.png"
        produto = "MORANGO"
        slogan = "O LADO ROMÂNTICO DE CLIGHT."
        texto= "<p>2De rosa, você está feliz. E mais do que isso, está também romântica.</p><p>Hoje você deve explorar esse seu lado para deixar a vida mais leve, fazendo só o que vai arrancar lindos sorrisos. E, se tiver alguém, aproveite para viver momentos à dois, com tudo que você tem direito.<p>Curta esse momento com toda a leveza. Espalhe amor por onde for.</p><p>Até porque o amor deixa todo mundo feliz.</p>"

    elif palavra == "sincera":
        mpalavra = "SINCERA"
        cor = "AZUL"
        mclass = "sincera"
        image = "app/imagens/produto-maracuja.png"
        produto = "MARACUJÁ"
        slogan = "O LADO ROMÂNTICO DE CLIGHT."
        texto= "<p>2De rosa, você está feliz. E mais do que isso, está também romântica.</p><p>Hoje você deve explorar esse seu lado para deixar a vida mais leve, fazendo só o que vai arrancar lindos sorrisos. E, se tiver alguém, aproveite para viver momentos à dois, com tudo que você tem direito.<p>Curta esse momento com toda a leveza. Espalhe amor por onde for.</p><p>Até porque o amor deixa todo mundo feliz.</p>"

    elif palavra == "tranquila":
        mpalavra = "TRANQUILA"
        cor = "AZUL"
        mclass = "tranquila"
        image = "app/imagens/produto-maracuja.png"
        produto = "MARACUJÁ"
        slogan = "O LADO ROMÂNTICO DE CLIGHT."
        texto= "<p>2De rosa, você está feliz. E mais do que isso, está também romântica.</p><p>Hoje você deve explorar esse seu lado para deixar a vida mais leve, fazendo só o que vai arrancar lindos sorrisos. E, se tiver alguém, aproveite para viver momentos à dois, com tudo que você tem direito.<p>Curta esse momento com toda a leveza. Espalhe amor por onde for.</p><p>Até porque o amor deixa todo mundo feliz.</p>"

    elif palavra == "confiante":
        mpalavra = "CONFIANTE"
        cor = "AZUL"
        mclass = "confiante"
        image = "app/imagens/produto-maracuja.png"
        produto = "MARACUJÁ"
        slogan = "O LADO ROMÂNTICO DE CLIGHT."
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
