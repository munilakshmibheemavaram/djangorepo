from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """Model representing a user profile."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        """String for representing the UserProfile object."""
        return self.user.username


class Post(models.Model):
    """Model representing a post."""
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String for representing the Post object."""
        return self.title


class Comment(models.Model):
    """Model representing a comment."""
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String for representing the Comment object."""
        return f'Comment by {self.author.username} on {self.post.title}'
