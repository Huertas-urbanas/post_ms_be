from django.db import models

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image =  models.URLField(blank=True)
    #category = 