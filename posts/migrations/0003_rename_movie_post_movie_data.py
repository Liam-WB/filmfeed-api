# Generated by Django 3.2.24 on 2024-03-21 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_movie'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='movie',
            new_name='movie_data',
        ),
    ]