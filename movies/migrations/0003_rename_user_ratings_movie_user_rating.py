# Generated by Django 3.2.24 on 2024-05-03 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20240503_1146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='user_ratings',
            new_name='user_rating',
        ),
    ]
