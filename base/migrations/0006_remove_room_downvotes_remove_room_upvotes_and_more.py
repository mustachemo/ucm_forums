# Generated by Django 5.0.4 on 2024-05-05 06:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_message_downvotes_message_upvotes_room_downvotes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='downvotes',
        ),
        migrations.RemoveField(
            model_name='room',
            name='upvotes',
        ),
        migrations.AddField(
            model_name='room',
            name='downvotes',
            field=models.ManyToManyField(blank=True, related_name='room_downvotes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='room',
            name='upvotes',
            field=models.ManyToManyField(blank=True, related_name='room_upvotes', to=settings.AUTH_USER_MODEL),
        ),
    ]
