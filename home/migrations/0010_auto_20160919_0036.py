# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-18 23:36
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_mediapage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediapage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('media', wagtail.wagtailcore.blocks.StructBlock((('media', wagtail.wagtailcore.blocks.StreamBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()),))),))),)),
        ),
    ]
