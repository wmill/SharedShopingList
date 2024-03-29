# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shoppinglist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingitem',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shoppingitem',
            name='name',
            field=models.CharField(max_length=400),
            preserve_default=True,
        ),
    ]
