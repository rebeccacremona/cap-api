# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-05 17:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.template.defaultfilters import slugify


class Migration(migrations.Migration):
    dependencies = [
        ('capi_project', '0018_auto_20170105_1733'),
    ]

    def court_forwards_func(apps, schema_editor):
        """
            1. iterate through cases
            2. create new Court if none exists by that name
            3. add jurisdiction foreign key, name_abbreviation, slug
        """
        Case = apps.get_model('capi_project', 'Case')
        Court = apps.get_model('capi_project', 'Court')

        for case in Case.objects.all():
            court, created = Court.objects.get_or_create(name=case.court, jurisdiction=case.jurisdiction)
            court.name_abbreviation = case.court_abbreviation
            court.slug = slugify(court.name_abbreviation)
            court.save()
            case.court_name = court
            case.save()

    operations = [
        migrations.RunPython(court_forwards_func)
    ]