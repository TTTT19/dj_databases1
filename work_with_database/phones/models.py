from django.db import models
from django.views.generic import ListView


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.TextField()
    price = models.IntegerField()
    image = models.TextField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.TextField()
