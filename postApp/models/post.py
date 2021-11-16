from django.db import models

class Post(models.Model):
    id    = models.AutoField(primary_key=True)
    user  = models.IntegerField(null=True)
    text  = models.TextField()
    date  = models.DateTimeField(auto_now_add=True, null=True)
    image = models.URLField(blank=True)

    def datepublished(self): return self.date.strftime('%d %b %Y' )