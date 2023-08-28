
from django.db import models
from django.forms import ImageField
from django.contrib.auth.models import User

# Create your models here.
class Model_category(models.Model):
    category_name = models.CharField(max_length = 50)
    sub_category_name = models.CharField(max_length = 50)
    category_image = models.ImageField(upload_to='./static/image')
    tag = models.CharField(max_length = 50)

class Model_details(models.Model):
    model_name = models.CharField(max_length = 50)
    who_aploaded = models.CharField(max_length = 50)
    short_discription = models.CharField(max_length = 100)
    category = models.ForeignKey(Model_category,on_delete=models.CASCADE)
    stl_model_image = models.ImageField(upload_to='./static/image')
    stl_file = models.FileField(upload_to='./static/stl')
    model_discription = models.TextField(max_length=2000)
    model_tag = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

