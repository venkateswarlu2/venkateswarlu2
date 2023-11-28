from django.db import models

# myapp/models.py
from django.db import models

class SignUp(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, default='')
    password = models.CharField(max_length=255)
    password1 = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.full_name


