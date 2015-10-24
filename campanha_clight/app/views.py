from django.shortcuts import render

# Create your views here.
def cor(request):
    palavra = request.palavra
    if(palavra == "romantica"):
        palavra = "ROMÂNTICA"
        cor = "ROSA"

    context = {
        'cor': cor,
        'palavra': palavra,
    }
    return render(request,
                  'app/cor.html',
                  context=context)

