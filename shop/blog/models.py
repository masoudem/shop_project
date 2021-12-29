from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.crypto import get_random_string
from django.utils.text import slugify
from market_user.models import CustomUser



class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=CASCADE, primary_key=True)
    avatar = models.FileField(null=True,blank=True)

    def __str__(self):
        return self.user.email


class Category(models.Model):
    
    # parent = models.ForeignKey('self',on_delete=models.SET_NULL,blank=True,null=True)
    name = models.CharField('category name' ,max_length=255)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=72, verbose_name=("title"))
    slug = models.SlugField(unique=True, max_length=100, allow_unicode=True)
    description = models.CharField(max_length=255, blank=True,null=True)
    bodytext = models.TextField(verbose_name=("message"))
    image = models.FileField(null=True,blank=True)
    category = models.ManyToManyField('Category', verbose_name='category of this post')
    tag = models.ManyToManyField('Tag', blank=True)
    post_date = models.DateTimeField(verbose_name="post date", auto_now_add=True, blank=True)
    owner = models.ForeignKey(CustomUser,on_delete=models.CASCADE,verbose_name='post owner', blank=True, null=True)


    class Meta:
        verbose_name = ('post')
        verbose_name_plural = ('posts')
        ordering = ['-post_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            if Post.objects.filter(slug = self.slug):
                the_slug = get_random_string(8,'0123456789')
                self.slug = slugify(self.title + the_slug)
        return super(Post, self).save(*args, **kwargs)


class Comment(models.Model): 
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80) 
    email = models.EmailField() 
    body = models.TextField() 
    created = models.DateTimeField(auto_now_add=True) 

    class Meta: 
        ordering = ('created',) 

    def __str__(self): 
        return 'Comment by {} on {}'.format(self.name, self.post) 


class Tag(models.Model):
    tag_name = models.CharField(max_length=200, verbose_name=("tag"))
    
    class Meta: 
        ordering = ('tag_name',) 

    def __str__(self): 
        return self.tag_name 
    
