from django.db import models

# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=255, unique=True)
    instructions = models.TextField(null=True)

    def __str__(self) -> str:
        return self.title

class Ingredient(models.Model):
    ingredient = models.CharField(max_length=200)
    amount = models.IntegerField()
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
