# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('content', models.TextField()),
                ('set_date', models.DateTimeField(verbose_name='set date', auto_now_add=True)),
                ('last_activity', models.DateTimeField(verbose_name='last activity', auto_now=True)),
                ('likes', models.PositiveIntegerField(default=0, verbose_name='likes')),
                ('dislikes', models.PositiveIntegerField(default=0, verbose_name='dislikes')),
                ('solved', models.BooleanField(default=False, verbose_name='solved')),
                ('last_modified_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='answers_modified', null=True, verbose_name='last_modified_by')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(verbose_name='nazwa', max_length=100, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('content', models.TextField(verbose_name='content')),
                ('set_date', models.DateTimeField(verbose_name='set date', auto_now_add=True)),
                ('last_activity', models.DateTimeField(verbose_name='last activity', auto_now=True)),
                ('likes', models.PositiveIntegerField(default=0, verbose_name='likes')),
                ('dislikes', models.PositiveIntegerField(default=0, verbose_name='dislikes')),
                ('answer', models.ForeignKey(to='api.Answer', related_name='comments', null=True, verbose_name='answer', blank=True)),
                ('last_modified_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='comments_modified', null=True, verbose_name='last_modified_by')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(verbose_name='question', max_length=300, unique=True)),
                ('content', models.TextField(verbose_name='content')),
                ('set_date', models.DateTimeField(verbose_name='set date', auto_now_add=True)),
                ('last_activity', models.DateTimeField(verbose_name='last activity', auto_now=True)),
                ('solved', models.BooleanField(default=False, verbose_name='solved')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='views')),
                ('likes', models.PositiveIntegerField(default=0, verbose_name='likes')),
                ('dislikes', models.PositiveIntegerField(default=0, verbose_name='dislikes')),
                ('favorites', models.PositiveIntegerField(default=0, verbose_name='favorites')),
                ('category', models.ForeignKey(to='api.Category', related_name='questions', default=1, verbose_name='category')),
                ('last_modified_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='questions_modified', null=True, verbose_name='last_modified_by')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='questions', verbose_name='użytkownik')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(verbose_name='nazwa', max_length=100, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('questions', models.ManyToManyField(null=True, verbose_name='questions', blank=True, to='api.Question', related_name='tags')),
            ],
        ),
        migrations.CreateModel(
            name='UserPreferences',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('disliked_answers', models.ManyToManyField(null=True, verbose_name='disliked answers', blank=True, to='api.Answer', related_name='disliked_answers')),
                ('disliked_comments', models.ManyToManyField(null=True, verbose_name='disliked comments', blank=True, to='api.Comment', related_name='disliked_comments')),
                ('disliked_questions', models.ManyToManyField(null=True, verbose_name='disliked questions', blank=True, to='api.Question', related_name='disliked_questions')),
                ('favorite_questions', models.ManyToManyField(null=True, verbose_name='favorite questions', blank=True, to='api.Question', related_name='favorite_questions')),
                ('liked_answers', models.ManyToManyField(null=True, verbose_name='liked answers', blank=True, to='api.Answer', related_name='liked_answers')),
                ('liked_comments', models.ManyToManyField(null=True, verbose_name='liked comments', blank=True, to='api.Comment', related_name='liked_comments')),
                ('liked_questions', models.ManyToManyField(null=True, verbose_name='liked questions', blank=True, to='api.Question', related_name='liked_questions')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('picture', models.ImageField(default='profile_images/blank-profile.jpg', null=True, verbose_name='picture', blank=True, upload_to='profile_images')),
                ('created', models.DateTimeField(verbose_name='created', auto_now_add=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='question',
            field=models.ForeignKey(to='api.Question', related_name='comments', null=True, verbose_name='question', blank=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='comments', verbose_name='użytkownik'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='api.Question', related_name='answers', null=True, verbose_name='content', blank=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='answers', verbose_name='użytkownik'),
        ),
    ]
