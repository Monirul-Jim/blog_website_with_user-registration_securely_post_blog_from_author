from django.db import models
from categories.models import Category
from django.contrib .auth.models import User
# Create your models here.


class Post(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    # models.cascade is use for  when a author delete his profile then also delete all post
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
