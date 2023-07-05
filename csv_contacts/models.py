from django.db import models


class Contacts(models.Model):
    """Model for DB activities related to Contacts data from CSV imported and saved in DB"""
    id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    zip = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    image = models.URLField(max_length=200)
