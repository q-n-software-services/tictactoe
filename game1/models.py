from django.db import models

# Create your models here.


class results(models.Model):
    added_date = models.DateTimeField()
    text = models.CharField(max_length=200)


class button(models.Model):
    button1 = models.CharField(max_length=12)


