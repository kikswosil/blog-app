from django.db import models
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
    created = models.DateTimeField(auto_now_add = True)
    edited = models.DateTimeField(auto_now_add = True)
    published = models.IntegerField(choices = PUBLISHED_CHOICES)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def to_dict(self):
        return {
            'title': self.title,
            'slug': self.slug,
            'content': self.content,
            'author': self.author.username, #type: ignore
        }

    def text_matches_any(self, text):
        self_dict = self.to_dict()
        for key in self_dict:
            if text in self_dict[key]:
                return True
        return False


class Comment(models.Model):
    text = models.CharField(max_length = 200, unique = True)
    date_published = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
