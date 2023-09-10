from django.shortcuts import render,redirect
from .models import Card
from .forms import CardForm

def index(request):
   return render(request, 'gls/index.html')


def product(request):
   catinfo = Card.objects.all()
   return render(request, 'gls/catalog.html',{'cat':catinfo})


def about(request):
   return render(request, 'gls/about.html')


def contact(request):
   return render(request, 'gls/contact.html')


def add(request):
   error=''
   if request.method == 'POST':
      form = CardForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('catalog')
         
      else:
         error='Форма была неверной'
   
   form = CardForm
   
   data = {
      'form': form,
      'error':error,
   }
   
   
   
   return render(request, 'gls/add.html',data)

