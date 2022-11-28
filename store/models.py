from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(_('name'), max_length = 255, db_index = True)
    slug = models.SlugField(max_length = 255, unique = True)

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, 
        verbose_name = 'category',
        related_name = 'product', 
        on_delete = models.CASCADE
    )
    