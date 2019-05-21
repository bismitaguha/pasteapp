from django.db import models

# Create your models here.
class Paste(models.Model):
    name = models.CharField(max_length=63)
    content = models.TextField()
    url = models.CharField(max_length=127)
    uploader = models.CharField(max_length=63)

class Comment(models.Model):
    content = models.TextField()
    writer = models.CharField(max_length=63, null=True, blank=True)
    paste = models.ForeignKey(Paste, related_name='comment', on_delete=models.CASCADE)
