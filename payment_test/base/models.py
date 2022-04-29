from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class transaction(models.Model):
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)