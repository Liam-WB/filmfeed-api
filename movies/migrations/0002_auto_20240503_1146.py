# Generated by Django 3.2.24 on 2024-05-03 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='user_rating',
        ),
        migrations.AddField(
            model_name='movie',
            name='user_ratings',
            field=models.TextField(blank=True, default='[]'),
        ),
    ]
