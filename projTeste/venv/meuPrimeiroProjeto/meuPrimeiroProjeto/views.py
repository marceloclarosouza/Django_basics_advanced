from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return render(request, 'index.html')#troquei o HttpResponse pelo render

def articles(request, year):
    return HttpResponse(f'O numero passado foi: {str(year)}')

def lerDoBanco(nome):
    lista_nomes= [
        {"nome": "Ana", "idade": 22},
        {"nome": "Pedro", "idade": 25},
        {"nome": "Joaquim", "idade": 27}
    ]

    for pessoa in lista_nomes:
        if pessoa["nome"]==nome:
            return pessoa
    else:
        return {"nome": "Nao encontrado", "idade": 0}

def fname(request, nome):
    """Essa funcao chama a funcao lerDoBanco"""
    result = lerDoBanco(nome)
    if result["idade"]>0:
        return HttpResponse('A pessoa encontrada tem: ' + str(result["idade"]) + " anos")
    else:
        return HttpResponse('Pessoa nao encontrada')

def fname2(request, nome):
    idade = lerDoBanco(nome)["idade"]
    return render(request, 'pessoa.html', {'v_idade':idade})

