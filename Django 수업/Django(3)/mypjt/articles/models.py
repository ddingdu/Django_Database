from django.db import models

# Create your models here.
class Article(models.Model):
    # CharField : title을 문자열 형태로 나타내라. 길이 명시 해줘야함
    title = models.CharField(max_length=20)
    # Textfield는 길이 제한 없음
    content = models.TextField()


