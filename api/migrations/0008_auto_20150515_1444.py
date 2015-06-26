# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0007_auto_20150313_1054'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='object_id',
        ),
        migrations.AddField(
            model_name='answer',
            name='last_modified_by',
            field=models.ForeignKey(related_name='answers_modified', null=True, to=settings.AUTH_USER_MODEL, verbose_name='last_modified_by'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='answer',
            field=models.ForeignKey(related_name='comments', null=True, to='api.Answer', blank=True, verbose_name='answer'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='last_modified_by',
            field=models.ForeignKey(related_name='comments_modified', null=True, to=settings.AUTH_USER_MODEL, verbose_name='last_modified_by'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='question',
            field=models.ForeignKey(related_name='comments', null=True, to='api.Question', blank=True, verbose_name='question'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='last_modified_by',
            field=models.ForeignKey(related_name='questions_modified', null=True, to=settings.AUTH_USER_MODEL, verbose_name='last_modified_by'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='answer',
            name='dislikes',
            field=models.PositiveIntegerField(default=0, verbose_name='dislikes'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='answer',
            name='last_activity',
            field=models.DateTimeField(auto_now=True, verbose_name='last activity'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='answer',
            name='likes',
            field=models.PositiveIntegerField(default=0, verbose_name='likes'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(related_name='answers', null=True, to='api.Question', blank=True, verbose_name='content'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='answer',
            name='set_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='set date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='answer',
            name='solved',
            field=models.BooleanField(default=False, verbose_name='solved'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(related_name='answers', to=settings.AUTH_USER_MODEL, verbose_name='użytkownik'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='nazwa'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(verbose_name='content'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='dislikes',
            field=models.PositiveIntegerField(default=0, verbose_name='dislikes'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='last_activity',
            field=models.DateTimeField(auto_now=True, verbose_name='last activity'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='likes',
            field=models.PositiveIntegerField(default=0, verbose_name='likes'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='set_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='set date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='użytkownik'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.ForeignKey(related_name='questions', to='api.Category', default=3, verbose_name='category'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='content',
            field=models.TextField(verbose_name='content'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='dislikes',
            field=models.PositiveIntegerField(default=0, verbose_name='dislikes'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='favorites',
            field=models.PositiveIntegerField(default=0, verbose_name='favorites'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='last_activity',
            field=models.DateTimeField(auto_now=True, verbose_name='last activity'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='likes',
            field=models.PositiveIntegerField(default=0, verbose_name='likes'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='set_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='set date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='solved',
            field=models.BooleanField(default=False, verbose_name='solved'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=300, unique=True, verbose_name='question'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='user',
            field=models.ForeignKey(related_name='questions', to=settings.AUTH_USER_MODEL, verbose_name='użytkownik'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='views',
            field=models.PositiveIntegerField(default=0, verbose_name='views'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='nazwa'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='disliked_answers',
            field=models.ManyToManyField(related_name='disliked_answers', blank=True, null=True, verbose_name='disliked answers', to='api.Answer'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='disliked_comments',
            field=models.ManyToManyField(related_name='disliked_comments', blank=True, null=True, verbose_name='disliked comments', to='api.Comment'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='disliked_questions',
            field=models.ManyToManyField(related_name='disliked_questions', blank=True, null=True, verbose_name='disliked questions', to='api.Question'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='favorite_questions',
            field=models.ManyToManyField(related_name='favorite_questions', blank=True, null=True, verbose_name='favorite questions', to='api.Question'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='liked_answers',
            field=models.ManyToManyField(related_name='liked_answers', blank=True, null=True, verbose_name='liked answers', to='api.Answer'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='liked_comments',
            field=models.ManyToManyField(related_name='liked_comments', blank=True, null=True, verbose_name='liked comments', to='api.Comment'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='liked_questions',
            field=models.ManyToManyField(related_name='liked_questions', blank=True, null=True, verbose_name='liked questions', to='api.Question'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(null=True, blank=True, upload_to='profile_images', default='profile_images/blank-profile.jpg', verbose_name='picture'),
            preserve_default=True,
        ),
    ]
