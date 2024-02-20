# Generated by Django 3.2.24 on 2024-02-20 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_genre_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('Action', 'Action'), ('Horror', 'Horror'), ('Comedy', 'Comedy'), ('Drama', 'Drama'), ('Fantasy', 'Fantasy'), ('Thriller', 'Thriller'), ('Romance', 'Romance'), ('Western', 'Western'), ('Adventure', 'Adventure'), ('Science fiction', 'Science fiction'), ('Crime', 'Crime'), ('Animation', 'Animation'), ('Documentary', 'Documentary'), ('Mystery', 'Mystery'), ('History', 'History'), ('Sports', 'Sports'), ('Musical', 'Musical'), ('News', 'News')], default='Action', max_length=15),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(blank=True, default='../default_post_rgq6aq', upload_to='images/'),
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
    ]
