from django.db import models



class Card(models.Model):
   img = models.ImageField(upload_to='images/')
   title = models.CharField('Название',max_length=45)
   start = models.CharField('Тираж',max_length=45)
   desc = models.TextField('Описание')
   
   def __str__(self):
      return self.title
   
   class Meta:
      verbose_name = 'Товар'
      verbose_name_plural = 'Товары'
