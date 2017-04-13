from django.db import models

class Legislator(models.Model):
    name = models.CharField(max_length=50)
    state = models.CharField(max_length=10)
    cid = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
