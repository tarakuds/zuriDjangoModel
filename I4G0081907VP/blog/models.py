from django.db import models
from django.contrib.auth import get_user_model

class Post(models.Model):
    Title = models.CharField(max_length=200)
    text = models.TextField()
    Author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    Author = models.TextField()
    Created_date = models.DateField()
    Published_date = models.DateField() 
    