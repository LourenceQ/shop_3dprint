from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.charField(max_length=200,deb_inex=200);
    slug = models.SlugField(,ax_length=200, unique=True);
