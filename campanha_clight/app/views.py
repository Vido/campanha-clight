from django.shortcuts import render

# Create your views here.
def cor(request, palavra):
    if(palavra == "romantica"):
        mpalavra = "ROMÂNTICA"
        cor = "ROSA"
        mclass="romantica"

    context = {
        'cor': cor,
        'palavra': mpalavra,
        'class': mclass,
    }
    return render(request,
                  'app/cor.html',
                  context=context)

