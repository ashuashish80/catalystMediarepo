from django.db import models
# fileuploadapp/models.py
class Data(models.Model):
    # Define your fields here
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()
    # Add other fields as needed
