# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-30 18:18
from __future__ import unicode_literals

import blogoland.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Slug')),
                ('seo_title', models.CharField(blank=True, max_length=70, null=True, verbose_name='SEO Title')),
                ('seo_description', models.CharField(blank=True, max_length=160, null=True, verbose_name='SEO Meta Description')),
                ('seo_keywords', models.CharField(blank=True, max_length=160, null=True, verbose_name='SEO Meta Keywords')),
            ],
            options={
                'verbose_name': 'Categoty',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Slug')),
                ('seo_title', models.CharField(blank=True, max_length=70, null=True, verbose_name='SEO Title')),
                ('seo_description', models.CharField(blank=True, max_length=160, null=True, verbose_name='SEO Meta Description')),
                ('seo_keywords', models.CharField(blank=True, max_length=160, null=True, verbose_name='SEO Meta Keywords')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('publication_date', models.DateField(default=datetime.date.today, verbose_name='Publication Date')),
                ('is_visible', models.BooleanField(default=True, verbose_name='Visible')),
                ('category', models.ManyToManyField(blank=True, to='blogoland.Category')),
            ],
            options={
                'ordering': ['-publication_date', '-creation_date', 'slug'],
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('img_type', models.CharField(blank=True, choices=[('detail', 'Detail Image'), ('thumbnail', 'Thumbnail Image'), ('gallery', 'Gallery Image')], max_length=255, null=True, verbose_name='Image Type')),
                ('image', models.ImageField(max_length=255, upload_to=blogoland.models.get_image_path)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_set', to='blogoland.Post')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
    ]
