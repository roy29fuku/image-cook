from django.db import models

# Create your models here.
class ImageFile(models.Model):
    data = models.ImageField(upload_to='images')

