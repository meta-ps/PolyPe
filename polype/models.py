from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255,primary_key=True)
    walletAddress = models.CharField(max_length=255)

    def __str__(self):
        return str(self.walletAddress)
