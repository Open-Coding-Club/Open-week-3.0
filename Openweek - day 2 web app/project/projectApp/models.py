from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
