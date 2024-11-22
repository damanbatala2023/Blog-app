from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)  # Unique username
    email = models.EmailField(unique=True)  # Unique email
    password = models.CharField(max_length=100)  # Store hashed password (Django manages this separately in auth)
    

    def __str__(self):
        return self.username  # String representation for easier debugging
