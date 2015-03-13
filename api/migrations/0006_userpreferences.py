# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0005_auto_20150313_1027'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPreferences',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('disliked_answers', models.ManyToManyField(null=True, blank=True, to='api.Answer', related_name='disliked_answers')),
                ('disliked_comments', models.ManyToManyField(null=True, blank=True, to='api.Comment', related_name='disliked_comments')),
                ('disliked_questions', models.ManyToManyField(null=True, blank=True, to='api.Question', related_name='disliked_questions')),
                ('favorite_questions', models.ManyToManyField(null=True, blank=True, to='api.Question', related_name='favorite_questions')),
                ('liked_answers', models.ManyToManyField(null=True, blank=True, to='api.Answer', related_name='liked_answers')),
                ('liked_comments', models.ManyToManyField(null=True, blank=True, to='api.Comment', related_name='liked_comments')),
                ('liked_questions', models.ManyToManyField(null=True, blank=True, to='api.Question', related_name='liked_questions')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
