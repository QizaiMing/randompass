from django.shortcuts import render
from .wordlist import wordlist
from .passgenerator import generate
from .dicegenerator import diceware
from django.http import JsonResponse

def home_view(request, *args, **kwargs):
    template_name = 'home.html'
    context = {}
    if request.method == 'POST':
        if request.POST.get('dictionary') == 'wordlist':
            password = generate()
            context['password'] = password
        else:
            password = diceware()
            context['diceware'] = password
    
    return render(request, template_name, context)

def wordlist_api(request):
    return JsonResponse({'method': 'wordlist' ,'password': generate()})

def diceware_api(request):
    return JsonResponse({'method': 'diceware','password': diceware()})
