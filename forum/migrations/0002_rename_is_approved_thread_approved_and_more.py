# Generated by Django 4.2.17 on 2025-01-14 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thread',
            old_name='is_approved',
            new_name='approved',
        ),
        migrations.AlterField(
            model_name='thread',
            name='related_article_url',
            field=models.URLField(blank=True, help_text='Optional: Paste the link to a related article.', max_length=250, null=True),
        ),
    ]