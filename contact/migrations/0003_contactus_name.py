# Generated by Django 3.2.24 on 2024-04-26 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20240425_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='name',
            field=models.CharField(default='default', max_length=255),
            preserve_default=False,
        ),
    ]
