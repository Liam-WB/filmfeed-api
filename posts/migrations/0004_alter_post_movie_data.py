# Generated by Django 3.2.24 on 2024-03-21 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_rename_movie_post_movie_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='movie_data',
            field=models.TextField(blank=True),
        ),
    ]
