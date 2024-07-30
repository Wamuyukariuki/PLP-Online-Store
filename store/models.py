from django.db import models
from django.urls import reverse
from category.models import Category


class Products(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(null=True, blank=True, max_length=10000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def get_url(self):
        return reverse('product_details', args=[self.category.slug, self.slug])  # Corrected 'slag' to 'slug'

    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
