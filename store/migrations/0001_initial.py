# Generated by Django 4.1.3 on 2022-11-28 14:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='name')),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('artist', models.CharField(default='admin', max_length=255, verbose_name='artist')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('image', models.ImageField(upload_to='images/', verbose_name='image')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='price')),
                ('in_stock', models.BooleanField(default=True, verbose_name='in_stock')),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='store.category', verbose_name='category')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ('-created',),
            },
        ),
    ]
