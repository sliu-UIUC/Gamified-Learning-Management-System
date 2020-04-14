from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model): #check database created: python manage.py sqlmigrate blog 0001 
  title = models.CharField(max_length=100)
  content = models.TextField()
  date_posted = models.DateTimeField(default=timezone.now) #function name instead of function
  #one to many: a user can have multiple posts, but one post one user
  author = models.ForeignKey(User, on_delete=models.CASCADE) #what we are going to do to certain posts if user is deleted

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('post-detail', kwargs={'pk':self.pk})