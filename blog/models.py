from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import BooleanField
from django_jalali.db import models as jmodels
from django.urls import reverse
from slugify import slugify    #unicode-slugify


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(post_status='published')



class Post(models.Model):
    POST_STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('rejected', 'Rejected'),
    )

    title = models.CharField(max_length=100, verbose_name='Title')
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts',verbose_name='Author')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Slug')
    post_status = models.CharField(max_length=20,default='draft',choices=POST_STATUS_CHOICES, verbose_name='Post Status')
    created = jmodels.jDateTimeField(auto_now_add=True)
    updated = jmodels.jDateTimeField(auto_now=True)
    selected = BooleanField(default=False, verbose_name='Is Selected')

    objects = jmodels.jManager()
    published = PublishedManager()
    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-created']
        verbose_name='Post'
        verbose_name_plural='Posts'

    def save(self, *args, **kwargs):
        self.slug = f"{slugify(self.title)}-{self.id}"
        return super().save(*args,**kwargs)


    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    objects = jmodels.jManager()

    class Meta:
        verbose_name='New'
        verbose_name_plural='News'

    def __str__(self):
        return self.title


class Comment(models.Model):
    COMMENT_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('published', 'Published'),
        ('rejected', 'Rejected'),
        ('spam', 'Spam'),
    )

    title = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(auto_now_add=True)
    comment_status = models.CharField(max_length=20, default='pending', choices=COMMENT_STATUS_CHOICES)
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=11,verbose_name='Phone Number')

    objects = jmodels.jManager()
    published = PublishedManager()

    class Meta:
        ordering = ['-created']
        verbose_name='Comment'
        verbose_name_plural='Comments'

    def __str__(self):
        return self.post.title
