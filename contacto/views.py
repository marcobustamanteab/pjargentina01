from django.shortcuts import render
#from contacto.models import Contacto

# Create your views here.
def contacto(request):
    return render(request,"contacto/contacto.html")