from django.db import models

# Create your models here.
# class 괄호 안에 적는 것 = 상속
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()



