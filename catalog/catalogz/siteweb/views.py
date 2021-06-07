from django.shortcuts import render, redirect
from . import models 
from prestations import models as models_prestations
import re
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')

@csrf_exempt
def envoi(request):
    success = True
    text = ''
    if request.method == 'POST':
        name = request.Post.get('name')
        email = request.Post.get('email')
        message = request.Post.get('message')

        if email.isspace() or email == '' or message.isspace() or message == '':
            success = False
            text = 'Veuillez remplir les champs vides'
        elif not re.fullmatch('(/w/.?)+@(/w/.?)+/.[A-Za-z]{2,3}', email):
            success = False
            text = 'Veuillez saisir un email valide'
        else:
            contacte = models.Contact(name= name, message= message, email=email)
            contacte.save()
            text = 'Votre message a bien été enregistré'

    datas = {
        'succes' : success,
        'text' : text
    }

    return JsonResponse(datas, safe=False)