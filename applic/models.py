from django.db import models

# Create your models here.
from django.db import models
from ckeditor.fields import RichTextField # импорт ckeditor

# Create your models here.
class MyAutoId(models.Model):
    class Meta():
        db_table = 'myautoid_app'

    title_myautoid = models.CharField(max_length=200)
    #text_myautoid = models.TextField(blank=True)
    text_redactor = RichTextField(blank=True) # указание creditor в самой модели

    def __unicode__(self):
        return self.title_myautoid