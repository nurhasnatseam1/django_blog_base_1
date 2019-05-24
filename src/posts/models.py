from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings



def upload_location(instance,filename):
    return f"images/posts/{instance.slug}/{filename}"
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=40)
    slug=models.SlugField(unique=True,default=None)
    content=models.TextField()
    publish=models.BooleanField()
    timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)
    updated=models.DateTimeField(auto_now=True,auto_now_add=False)
    image=models.ImageField(upload_to=upload_location,null=True,blank=True,height_field='height_field',width_field='width_field')
    height_field=models.IntegerField(default=0)
    width_field=models.IntegerField(default=0)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=1)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:posts_detail',kwargs={'slug':self.slug})



def create_slug(instance,new_slug=None):
    slug=slugify(instance.title)
    if new_slug is not None:
        slug=new_slug
    qs=Post.objects.filter(slug=slug).order_by('-id')
    exists=qs.exists()
    if exists:
        new_slug=f"{slug}-{qs.first().id}"
        return create_slug(instance,new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=create_slug(instance)
    

pre_save.connect(pre_save_post_receiver,sender=Post)


