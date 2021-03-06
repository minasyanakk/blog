from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

TELEGRAM = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = HTMLField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    telegram = models.IntegerField(choices=TELEGRAM, default=0)
    cover = models.ImageField(upload_to='images/',blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title