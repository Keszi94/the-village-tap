from django import template

register = template.Library()


@register.filter
def cloudinary_small(url):
    # Only apply if URL is valid
    if not url or 'upload' not in url:
        return url
    # Safely insert after the first 'upload/' occurrence
    return url.replace('/upload/', '/upload/w_600,f_auto,q_auto/')
