from django.db import models

# Create your models here.

class Destination(models.Model): 
    # id: int #by default table has primary key field so there is no need to create id field in model.
    name= models.CharField(max_length=100)
    offer= models.BooleanField(default=False)
    # If you using Image related work you need to install a package that manages images. "python -m pip install Pillow".
    img = models.ImageField(upload_to='pics')
    desc= models.TextField() # Because it can be longer.
    price= models.IntegerField()
