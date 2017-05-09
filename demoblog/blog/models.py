from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField

class Tag(models.Model):
    """ A model representing a tag of a blog post """
    slug = models.CharField(max_length=50)

    def __str__(self):
        return self.slug

class Post(models.Model):
    """ A model representing a blog post """
    
    title = models.CharField(max_length=200)
    content = RichTextField()
    image = models.ImageField(upload_to='images/')
    tags = models.ManyToManyField(Tag, related_name='posts')
    author = models.ForeignKey(User, related_name='posts')
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)
    
    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)