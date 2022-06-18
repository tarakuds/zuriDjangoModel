from django.db import models

# Create your models here.
# class author (models.Model):
#     name = models.get_user_model()

    # def __str__(self) -> str:
    #     return self.name

class Post(models.Model):
    Title = models.CharField(max_length=200)
    text = models.TextField()
    # Author = models.ForeignKey(author, on_delete=models.CASCADE)
    Author = models.TextField()
    Created_date = models.DateField()
    Published_date = models.DateField() 
    