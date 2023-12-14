from django.db import models

# Create your models here.

class Contacts(models.Model):
    contact_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    def __str__(self):
      return f"{self.first_name} {self.last_name}"
