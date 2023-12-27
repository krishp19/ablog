from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self) -> str:
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('article-detail',args=(str(self.id)))
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE ,related_name='comments')
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return '%s - %s' % (self.post.title, self.name)
    
    def get_absolute_url(self):
        return reverse('add_comment',args=(str(self.id),))