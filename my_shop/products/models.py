from django.db import models

# Create your models here.
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    amount = models.IntegerField(null=True)


def __str__(self):
    return f"{self.name} {self.type}"
