# Generated by Django 5.0.6 on 2024-07-01 21:53

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('c', 'Caffe'), ('i', 'IcePack'), ('d', 'Dessert'), ('s', 'Snack'), ('s', 'Smoothie'), ('m', 'Mocktile')], max_length=225)),
                ('description', models.TextField(blank=True, verbose_name='description')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='description')),
                ('name', models.CharField(max_length=225, verbose_name='name')),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='price')),
                ('image', models.ImageField(blank=True, upload_to='media/snack_images/', verbose_name='image')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='menu.category', verbose_name='category')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='top_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='menu.product', verbose_name='top_product'),
        ),
    ]
