from django.db import models

class Legislator(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    state = models.CharField(max_length=10)
    state_name = models.CharField(max_length=20)
    cid = models.CharField(max_length=15)
    pid = models.CharField(max_length=15)
    chamber = models.CharField(max_length=25)
    term_start = models.CharField(max_length=15)
    term_end = models.CharField(max_length=15)
    party = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
