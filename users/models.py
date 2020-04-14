from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE) #one way delete profile when user is deleted
  image = models.ImageField(default='default.jpg', upload_to='profile_pics')
  money = models.PositiveIntegerField(default=5)


  def __str__(self): #custom display
    return f'{self.user.username} Profile'

  def save(self, *args, **kwargs):
    super(Profile, self).save(*args, **kwargs)

    img = Image.open(self.image.path)

    if img.height>300 or img.width>300: 
      output_size = (300, 300)
      img.thumbnail(output_size)
      img.save(self.image.path)