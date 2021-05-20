from django.db import models
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=140)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
                        "portalapp:category_detail",
                        kwargs={'category_slug': self.slug}
                        )


def upload_article_image_folder(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[-1]
    return "{}/{}".format(instance.slug, filename)


class Article(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to=upload_article_image_folder)
    content = models.TextField()
    release_date = models.DateTimeField(auto_now=True)
    likes_count = models.PositiveIntegerField(default=0)
    dislikes_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "Статья '{}' из категории '{}'".format(self.title, self.category.name)

    def get_absolute_url(self):
        return reverse("portalapp:article_detail", kwargs={'article_slug': self.slug})
