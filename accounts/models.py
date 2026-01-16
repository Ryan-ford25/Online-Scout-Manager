from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Patrols(models.Model):
    name = models.CharField(max_length=50)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    role = models.CharField(max_length=20)
    patrol = models.ForeignKey(Patrols, on_delete=models.SET_NULL, null=True, blank=True)
                               

    def __str__(self):
        return f"{self.user.username} Profile"
    
