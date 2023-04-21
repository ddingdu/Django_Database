from django.db import models

# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()


    def __str__(self):
        return f'{self.id}번째글 - {self.title}'