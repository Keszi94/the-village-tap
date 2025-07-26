from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify


# Create your models here.


CATEGORY_CHOICES = [
    ('news', 'General News'),
    ('traffic', 'Traffic'),
    ('obituaries', 'Obituaries'),
    ('wedding', 'Wedding Announcements'),
    ('history', 'Village History'),
    ('achievements', 'Village Achievements'),
]

DEFAULT_IMAGE_URL = (
    "https://res.cloudinary.com/diz4bvzz9/image/upload/"
    "v1739203594/default_lqlg2e.webp"
)


class Article(models.Model):
    """
    Represents a news article posted on the site.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="articles")
    category = models.CharField(
         max_length=50, choices=CATEGORY_CHOICES, default='news')
    blurb = models.TextField(help_text="A short summary of the article.")
    content = models.TextField()
    sources = models.TextField(blank=True, help_text="Optional: list any and"
                               "all resources used in the article.")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    image = CloudinaryField('image', blank=True, null=True)

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

    def save(self, *args, **kwargs):
        """
        Automatically generates a slug from the title if not provided
        and ensures it's URL-friendly.
        """
        if not self.slug:
            self.slug = slugify(self.title)

        # Apply default image if missing
        if not self.image:
            self.image = DEFAULT_IMAGE_URL

        super().save(*args, **kwargs)
