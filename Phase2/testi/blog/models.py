from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils import timezone

class BlogModel(models.Model):
    title=models.CharField(max_length=100, null=False)
    description=models.TextField(null=True)
    published_at=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        db_table="posts"
        ordering=["-published_at"]
    
    def __str__(self):
        return self.title