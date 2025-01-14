from django.db import models
from django.contrib.auth.models import User

# Create your models here.


CATEGORY_CHOICES = [
    ('news', 'General News'),
    ('traffic', 'Traffic'),
    ('obituaries', 'Obituaries'),
    ('wedding', 'Wedding Announcements'),
    ('history', 'Village History'),
    ('achievements', 'Village Achievements'),
]


class Article(models.Model):
    """
    Represents a news article posted on the site.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True) # will be filled out automatically later
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='news')
    blurb = models.TextField(help_text="A short summary of the article.")
    content = models.TextField()
    sources = models.TextField(
        blank=True,
        help_text="Optional: list any and all resources used in the article.")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    # Status Field
    DRAFT = 1
    PUBLISHED = 2
    ARCHIVED = 3
    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
        (ARCHIVED, 'Archived'),
    ]
    status = models.IntegerField(choices=STATUS_CHOICES, default=DRAFT)


    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"{self.title} | written by {self.author}"