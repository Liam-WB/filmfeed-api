# Generated by Django 3.2.24 on 2024-05-03 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_rename_user_rating_movie_user_ratings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='user_ratings',
            field=models.JSONField(blank=True, default='[]'),
        ),
    ]