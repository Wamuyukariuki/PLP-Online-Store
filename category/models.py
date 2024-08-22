from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    keyword = models.TextField()
    image = models.ImageField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    STATUS = (
        ('True', 'True'),
        ('False', 'False')
    )
    status = models.CharField(max_length=10, choices=STATUS, default='True')

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('category:products_bycategory', args=[self.slug])

    def __str__(self):
        return self.name
