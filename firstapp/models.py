from django.db import models

class Account(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=25)