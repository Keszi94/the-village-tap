from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from news.models import Article


# Create your models here.


class Thread(models.Model):
    """
    Represents a thread in the forum
    """
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="threads")
    description = models.TextField()
    related_article_url = models.URLField(max_length=250, blank=True, null=True, help_text="Optional: Paste the link to a related article.")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    # Status Field
    PENDING = 1
    APPROVED = 2
    REJECTED = 3
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
    ]
    status = models.IntegerField(choices=STATUS_CHOICES, default=PENDING)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.title} | created by {self.author}"

    def save(self, *args, **kwargs):
        if not self.slug: # generates the slug if it's not already set
            self.slug = slugify(self.title)
        super().save(*args, **kwargs) # calls on the parent class's safe method    


class Comment(models.Model):
    thread = models.ForeignKey('forum.Thread', on_delete=models.CASCADE, related_name='comment')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Comment by {self.author.username} on {self.thread.title}"





        