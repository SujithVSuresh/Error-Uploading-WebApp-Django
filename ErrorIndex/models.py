from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class ErrorListing(models.Model):

    MODE = (
        ('Public', 'Public'),
        ('Private', 'Private'),
    )
    error_body = models.TextField()
    error_description = models.TextField(default='')
    error_reason = models.TextField()
    error_solution = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=timezone.now)
    like = models.ManyToManyField(User, blank=True, related_name='like')
    dislike = models.ManyToManyField(User, blank=True, related_name='dislike')
    mode = models.CharField(max_length=200, null=True, choices=MODE)

    def __str__(self):
        return self.error_body