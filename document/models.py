from django.db import models
# if import not working shift +control+ p select python interpretor and use your virtual env if you have created 
# Create your models here.
class Document(models.Model):
    title= models.CharField(max_length=255)
    content=models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("title",) 