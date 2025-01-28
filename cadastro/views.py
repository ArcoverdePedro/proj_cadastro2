from django.shortcuts import render
from django.http import JsonResponse
from .utils import validador
from .models import Pessoa
from django.views.decorators.csrf import csrf_exempt
import requests
from django.core.validators import EmailValidator

# Create your views here.


@csrf_exempt
def home(request):
    return render(request, 'home.html')

@csrf_exempt
def validarcpf(request):
    cpf = request.POST.get('cpf')
    if validador(cpf):
        return JsonResponse({'status': "ok"})
    else:
        return JsonResponse({'status': "erro"})

@csrf_exempt
def validaremail(request):
    email = request.POST.get('email')
    validator = EmailValidator()
    try:
        validator(email)
        return JsonResponse({'status': "ok"})
    except:
        return JsonResponse({'status': "erro"})
    
@csrf_exempt
def buscarcep(request):
    if request.method == 'POST':
        cep_number = request.POST.get('cep')
        #tenta puxar o cep da api do viacep
        try :
            #faz a requisição e pega o json colocando na variavel data
            response = requests.get(f'https://viacep.com.br/ws/{cep_number}/json/') 
            data = response.json()
            return JsonResponse(data)
        except:
            #se der erro na requisição, retorna erro = true (aplicando a mesma lógica da api do viacep)
            return JsonResponse({'erro': 'true'})

@csrf_exempt 
def cadastro(request):
    return render(request, 'cadastro.html')

@csrf_exempt
def cadastrar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        cep = request.POST.get('cep')
        Telefone = request.POST.get('Telefone')
        pessoa = Pessoa(
            nome=nome,
            cpf=cpf,
            email=email,
            cep=cep, 
            Telefone=Telefone,
            )
        #pessoa.save()
        return render(request, 'dentro.html')
    
@csrf_exempt
def dentro(request):

    return render(request, 'dentro.html')
