from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(default='profile_default.jpg', upload_to='profile_images')
    bio = models.TextField(blank=True)
    contacts = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    # crop uploaded image's resolution to 600px
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # methods from PIL library
        photo = Image.open(self.photo.path)
        if photo.height > 600 or photo.width > 600:
            output_size = (600, 600)
            photo.thumbnail(output_size)
            photo.save(self.photo.path)
