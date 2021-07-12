from django.db import models

# Create your models here.


class User(models.Model):
    TYPE_TEMP = "temp"
    TYPE_BASIC = "basic"
    TYPE_PRO = "pro"

    TYPE_CHOICES = ((TYPE_TEMP, "Temp"), (TYPE_BASIC, "Basic"), (TYPE_PRO, "Pro"))

    uid = models.TextField()
    user_type = models.CharField(choices=TYPE_CHOICES, max_length=10)
