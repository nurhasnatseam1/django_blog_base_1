from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=40)
    content=models.TextField()
    publish=models.BooleanField()
    timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)
    updated=models.DateTimeField(auto_now=True,auto_now_add=False)
    image=models.FileField(upload_to='images/posts',null=True,blank=True)

    def __str__(self):
        return self.title