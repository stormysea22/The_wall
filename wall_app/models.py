from django.db import models
from login_app.models import User
import re
from datetime import datetime, timedelta, timezone

# Create your models here.
class Post(models.Model):
    post_message = models.TextField()
    user = models.ForeignKey(User, related_name="user_posts", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def age(self): 
        now = datetime.now()
        time_difference = datetime.now(timezone.utc) - self.created_at 
        age = int(time_difference.total_seconds() / 60)
        return age

class Comment(models.Model):
    user = models.ForeignKey(User, related_name="user_comments", on_delete = models.CASCADE)
    post = models.ForeignKey(Post, related_name="comment", on_delete = models.CASCADE)
    comment_message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def age(self): 
        now = datetime.now()
        time_difference = datetime.now(timezone.utc) - self.created_at 
        age = int(time_difference.total_seconds() / 60)
        return age