from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
PUBLISHED_CHOICES = (
    (0, 'DRAFT'),
    (1, 'PUBLISHED')
)

class Post(models.Model):
    title = models.CharField(max_length = 200, unique = True)
    slug = models.SlugField(max_length = 200, unique = True)
    content = models.TextField(max_length = 1000)
    created = models.DateTimeField(timezone.now())
    edited = models.DateTimeField(timezone.now())
    published = models.IntegerField(choices=PUBLISHED_CHOICES)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

