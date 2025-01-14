from django.db import models
from django.contrib.auth.models import User
from news.models import Article


# Create your models here.


class Thread(models.Model):
    """
    Represents a thread in the forum
    """
    title = models.CharField(max_length=150, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="threads")
    content = models.TextField(help_text="The main content of the thread.")
    related_article_url = models.URLField(max_length=250, blank=True, null=True, help_text="Optional: Paste the link to a related article.")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


            

