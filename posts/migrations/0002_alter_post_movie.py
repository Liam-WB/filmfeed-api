# Generated by Django 3.2.24 on 2024-03-25 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='movie',
            field=models.TextField(blank=True),
        ),
    ]
