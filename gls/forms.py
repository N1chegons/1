from .models import  Card
from django.forms import ModelForm, TextInput,FileInput,Textarea



class CardForm(ModelForm):
   class Meta:
      model = Card
      fields = ['title','start','desc']
      
      widgets = {
         
         'img': FileInput(attrs={
            'class':'form-control add-cards',
         }),
         
         
         'title': TextInput(attrs={
            'class':'form-control add-cards',
            'placeholder':'Название товара',
         }),
         
         'start': TextInput(attrs={
            'class':'form-control add-cards',
            'value':'Тираж: от .. штук',
         }),

          'desc': Textarea(attrs={
            'class':'form-control add-cards',
            'placeholder':'Описание товара',
         }),
      }