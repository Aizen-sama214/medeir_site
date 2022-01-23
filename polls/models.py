from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Import(models.Model):
    img_name = models.CharField(max_length=200)
    #pub_date = models.DateTimeField('date published')
    image = models.FileField(upload_to='images/corrupted/')

    def __str__(self):
        return self.img_name

class Slice(models.Model):
    img_name = models.CharField(max_length=200)
    #pub_date = models.DateTimeField('date published')
    image = models.FileField(upload_to='images/slices/')

    def __str__(self):
        return self.img_name

