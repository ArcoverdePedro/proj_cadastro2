from django.shortcuts import render,redirect, get_object_or_404
from django.http import JsonResponse
from .utils import validador
from .models import Pessoa
import requests
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import EmailValidator

# Create your views here.


@csrf_exempt
def home(request):
    pessoas = Pessoa.objects.order_by('-id')
    return render(request, 'home.html', {'pessoas':pessoas})

@csrf_exempt 
def cadastro(request):
    return render(request, 'cadastro.html')

@csrf_exempt
def cadastrar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')

        cpf = request.POST.get('cpf')
        if not validador(cpf):
            response = JsonResponse({'erro': "cpf"})
            return response
        
        email = request.POST.get('email')
        try:
            validaremail = EmailValidator()
            validaremail(email)            
        except:
            return JsonResponse({'erro': "email"})
        
        cep = request.POST.get('cep')
        cep = cep.replace('-', '')
        if len(cep) == 8:
            try:
                int(cep)
                response = requests.get(f'https://viacep.com.br/ws/{cep}/json/').json()
                if "erro" in response:
                    return JsonResponse({'erro': "cep"})
            except:
                return response
        elif len(cep) != 8:
            response = JsonResponse({'erro': "cep"})
            return response
        
        telefone = request.POST.get('telefone')

        pessoa = Pessoa(
            nome=nome,
            cpf=cpf,
            email=email,
            cep=cep, 
            telefone=telefone,
            )
        pessoa.save()
        return redirect('home')

@csrf_exempt
def excluir(request, id):
    if request.method == 'POST':
        idpessoa = request.POST.get('id')
        pessoa_cadastrada = get_object_or_404(Pessoa, id = idpessoa)
        pessoa_cadastrada.delete()
    return redirect('home')

@csrf_exempt
def editar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')

        cpf = request.POST.get('cpf')
        if not validador(cpf):
            response = JsonResponse({'erro': "cpf"})
            return response
        
        email = request.POST.get('email')
        try:
            validaremail = EmailValidator()
            validaremail(email)            
        except:
            return JsonResponse({'erro': "email"})
        
        cep = request.POST.get('cep')
        cep = cep.replace('-', '')
        if len(cep) == 8:
            try:
                int(cep)
                response = requests.get(f'https://viacep.com.br/ws/{cep}/json/').json()
                if "erro" in response:
                    return JsonResponse({'erro': "cep"})
            except:
                return response
        elif len(cep) != 8:
            response = JsonResponse({'erro': "cep"})
            return response
        
        telefone = request.POST.get('telefone')

        pessoa = Pessoa(
            nome=nome,
            cpf=cpf,
            email=email,
            cep=cep, 
            telefone=telefone,
            )
        pessoa.save()
    return redirect('home')
