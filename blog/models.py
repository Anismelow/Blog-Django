from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.Charfield(max_length=255)
    slug = models.SlugField(max_length=255 ) # el slug ayuda a crear url amigables con el seo 
    bosy = models.TextField()
    
    def __str__(self):
        return self.title