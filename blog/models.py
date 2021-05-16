from django.db import models
from django.db.models import constraints
from authentication.models import User
from django.utils import timezone
# Create your models here.

class BlogPost(models.Model):
    VIEW_TYPE = (
        (1, 'Everyone'),
        (2, 'Only for Friends'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default = timezone.now)
    last_updated_at = models.DateTimeField(auto_now = True)
    content = models.TextField(null=True, blank=True)
    image = models.FileField(null=True, blank=True)
    view_type = models.PositiveSmallIntegerField(choices=VIEW_TYPE, default=1, blank=True)


    class Meta:
        ordering = ['-id',]


class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default = timezone.now)
    last_updated_at = models.DateTimeField(auto_now_add = True)
    content = models.TextField()

    class Meta:
        ordering = ['-id',]

class Like(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'post'], name="unique_likes")
        ]
        ordering = ['-id',]