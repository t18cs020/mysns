from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    icon = models.ImageField(upload_to='profiles',blank=True, null=True)

class Posts(models.Model):
    message = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    postedtime = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.message[:10]