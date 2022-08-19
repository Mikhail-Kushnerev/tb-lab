from django.db import models


class Info(models.Model):
    date = models.DateTimeField(auto_now=True)
    user_id = models.IntegerField()
    domen = models.CharField(max_length=200)
