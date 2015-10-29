from django.http import Http404
from django.shortcuts import render

from campanha_clight import settings

# Create your views here.

def compartilhe(request, palavra):
    context = __getType(palavra)
    context['SITE_URL'] = settings.SITE_URL

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
        cor_image = "vermelho"
        mclass = "impulsiva"
        image = "app/imagens/produto-morango.png"
        produto = "MORANGO"
        slogan = "O LADO IMPULSIVO DE CLIGHT."
        texto= "<p>Hoje ninguém te segura! Aproveite essa energia e ousadia para sair, explorar novos lugares ou conquistar novas metas.</p><p> Para cuidar da saúde, as dicas são Crossfit, corrida ou artes marciais para gastar toda essa energia. Haja pique!</p>"


    elif palavra == "linda":
        mpalavra = "LINDA"
        cor = "ROSA"
        cor_image = "rosa"
        mclass = "linda"
        image = "app/imagens/produto-manga.png"
        produto = "MANGA"
        slogan = "O LADO LINDO DE CLIGHT."
        texto= "<p>Hoje o dia pede bastante afeto e companhia agradável. Ninguém vai te convencer a acelerar seu ritmo!</p><p> Faça tudo do seu jeito e no seu tempo. No trabalho, você encanta os colegas e clientes com bastante competência e pé no chão.</p>"

    elif palavra == "extrovertida":
        mpalavra = "EXTROVERTIDA"
        cor = "AMARELO"
        cor_image = "amarelo"
        mclass = "extrovertida"
        image = "app/imagens/produto-abacaxigengibre.png"
        produto = "ABACAXI E GENGIBRE"
        slogan = "O LADO EXTROVERTIDO DE CLIGHT."
        texto= "<p>Agitação é a palavra do dia! O clima é de muita conversa e novidades, perfeito para se divertir.</p><p> O amor é favorecido com programas diferentes. Que tal jantar naquele restaurante de comida tailandesa? Vai ter assunto pra noite inteira.</p>"


    elif palavra == "vaidosa":
        mpalavra = "VAIDOSA"
        cor = "PINK"
        cor_image = "pink"
        mclass = "vaidosa"
        image = "app/imagens/produto-tealimao.png"
        produto = "TEA LIMÃO"
        slogan = "O LADO VAIDOSO DE CLIGHT."
        texto= "<p>Tem dias que a gente está de lua e acorda mais vaidosa do que todo mundo!</p><p> Hoje, cuidar da saúde contribui para que você se sinta mais confiante. Se alimentar bem, fazer esportes, alongamento e cuidar da pele são as dicas.</p>"

    elif palavra == "confiante":
        mpalavra = "CONFIANTE"
        cor = "BORDÔ"
        cor_image = "bordo"
        mclass = "confiante"
        image = "app/imagens/produto-tangerina.png"
        produto = "TANGERINA"
        slogan = "O LADO CONFIANTE DE CLIGHT."
        texto= "<p>Totalmente demais! Hoje você brilha mais do que ninguém e vai adorar ser o centro das atenções.</p><p> Capriche no visual e no cuidado com os cabelos. No trabalho, as posições de liderança vão cair muito bem e projetos são discutidos com paixão!</p>"

    elif palavra == "espontanea":
        mpalavra = "ESPONTÂNEA"
        cor = "VERDE"
        cor_image = "verde"
        mclass = "espontanea"
        image = "app/imagens/produto-limalimao.png"
        produto = "LIMA LIMÃO"
        slogan = "O LADO ESPONTÂNEO DE CLIGHT."
        texto= "<p>Uau, corpo e mente estão em total sintonia hoje e você consegue se comunicar melhor que ninguém.</p><p> O destaque é para a saúde: boa alimentação combinada com seu esporte preferido ou yoga já produzem aquela higiene mental e energética que você adora.</p>"

    elif palavra == "livre":
        mpalavra = "LIVRE"
        cor = "TURQUESA"
        cor_image = "turquesa"
        mclass = "livre"
        image = "app/imagens/produto-abacaxihortela.png"
        produto = "ABACAXI E HORTELÃ"
        slogan = "O LADO LIVRE DE CLIGHT."
        texto= "<p>Livre como o vento! Assim vai ser o seu dia. No amor, as coisas devem correr com tranquilidade e você poderá cativar quem você quiser, sem esforço.</p><p> Aproveite para fazer um programa romântico como um passeio ao luar e conversar a noite toda!</p>"

    elif palavra == "misteriosa":
        mpalavra = "MISTERIOSA"
        cor = "VIOLETA"
        cor_image = "violeta"
        mclass = "misteriosa"
        image = "app/imagens/produto-uva.png"
        produto = "UVA"
        slogan = "O LADO MISTERIOSO DE CLIGHT."
        texto= "<p>Hoje você está podendo! Estratégia é a palavra chave e você esconde o jogo, deixando todos fascinados por esse ar de mistério.</p><p> No amor, você está mais sexy e sedutora do que nunca! Paixões secretas e amores transformadores estão em alta.</p>"

    elif palavra == "otimista":
        mpalavra = "OTIMISTA"
        cor = "LARANJA"
        cor_image = "laranja"
        mclass = "otimista"
        image = "app/imagens/produto-laranja.png"
        produto = "LARANJA"
        slogan = "O LADO OTIMISTA DE CLIGHT."
        texto= "<p>É HOJE! Vai ser difícil alguém segurar seu entusiasmo e energia, mas mesmo seu jeito animado atrai muitos pretendentes.</p><p> Que tal uma balada com os amigos? As compromissadas vão adorar fazer uma viagem e explorar lugares novos com o seu amor.</p>"

    elif palavra == "poderosa":
        mpalavra = "PODEROSA"
        cor = "AZUL MARINHO"
        cor_image = "marinho"
        mclass = "poderosa"
        image = "app/imagens/produto-amoraframboesa.png"
        produto = "AMORA E FRAMBOESA"
        slogan = "O LADO PODEROSO DE CLIGHT."
        texto= "<p>Hoje o dia está perfeito para mostrar quem manda no pedaço!</p><p> O trabalho tem destaque e você colhe frutos com sua dedicação e responsabilidade. Afinal, se alguém pode chegar ao topo, essa pessoa é você.</p>"

    elif palavra == "zen":
        mpalavra = "ZEN"
        cor = "AZUL"
        cor_image = "azul"
        mclass = "zen"
        image = "app/imagens/produto-maracuja.png"
        produto = "MARACUJÁ"
        slogan = "O LADO ZEN DE CLIGHT."
        texto= "<p>Não existe ninguém mais autêntica que você! Totalmente relax, você tira de letra todos os desafios do dia.</p><p> Para cuidar da saúde, a pedida é yoga, pilates, tai-chi ou qualquer outra atividade que conecte seu corpo com mente e emoções.</p>"

    elif palavra == "apaixonada":
        mpalavra = "APAIXONADA"
        cor = "LILÁS"
        cor_image = "lilas"
        mclass = "apaixonada"
        image = "app/imagens/produto-pessego.png"
        produto = "TEA PÊSSEGO"
        slogan = "O LADO APAIXONADO DE CLIGHT."
        texto= "<p>Sua sensibilidade é cativante e hoje seu dia vai ser cheio de emoções.</p><p> O destaque vai para o amor: com esse seu jeito carinhoso e perceptivo, você sabe exatamente quem está interessado em você ou não. A energia de hoje faz com que seja fácil se apaixonar!</p>"

    else:
        raise Http404("Page not Found")

    context = {
        'cor': cor,
        'cor_image': cor_image,
        'palavra': mpalavra,
        'class': mclass,
        'image': image,
        'produto': produto,
        'slogan': slogan,
        'texto': texto
    }

    return context
