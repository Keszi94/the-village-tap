# Generated by Django 4.2.17 on 2025-01-14 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_rename_is_approved_thread_approved_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thread',
            name='related_article',
        ),
    ]