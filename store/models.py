from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

User = get_user_model()


class Category(models.Model):
    name = models.CharField(_('name'), max_length = 255, db_index = True)
    slug = models.SlugField(max_length = 255, unique = True)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def get_absolute_url(self):
        return reverse("store:category_list", args = [self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, 
        verbose_name = 'category',
        related_name = 'product', 
        on_delete = models.CASCADE
    )
    created_by = models.ForeignKey(
        User, 
        on_delete = models.CASCADE, 
        related_name = 'creator'
    )
    name = models.CharField(_('name'), max_length = 255)
    artist = models.CharField(_('artist'), max_length = 255, default='admin')
    description = models.TextField(_('description'), blank = True)
    image = models.ImageField(_('image'), upload_to = 'images/')
    slug = models.SlugField(max_length = 255, unique = True)
    price = models.DecimalField(_('price'), max_digits = 4, decimal_places = 2)
    in_stock = models.BooleanField(_('in_stock'), default = True)
    is_active = models.BooleanField(_('is_active'), default = True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        ordering = ('-created', )

    def get_absolute_url(self):
        return reverse("store:product_detail", args = [self.slug])
    

    def __str__(self):
        return self.name
