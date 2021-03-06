# Generated by Django 2.2 on 2019-11-05 19:53

from django.db import migrations, models
import django.db.models.deletion
import portalapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to=portalapp.models.upload_article_image_folder)),
                ('content', models.TextField()),
                ('release_date', models.DateTimeField(auto_now=True)),
                ('likes_count', models.PositiveIntegerField(default=0)),
                ('dislikes_count', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portalapp.Category')),
            ],
        ),
    ]
