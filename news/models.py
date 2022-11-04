from django.db import models

# Create your models here.
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)


class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
