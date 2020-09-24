from django.http import HttpResponse

def hello(request):
    return HttpResponse('Olá mundo!')

def articles(request, year):
    return HttpResponse(f'O numero passado foi: {str(year)}')

