# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-09-25 14:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import parler.models
import shuup.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available_from', models.DateTimeField(blank=True, help_text='Set an available from date to restrict the page to be available only after a certain date and time. This is useful for pages describing sales campaigns or other time-sensitive pages.', null=True, verbose_name='available from')),
                ('available_to', models.DateTimeField(blank=True, help_text='Set an available to date to restrict the page to be available only after a certain date and time. This is useful for pages describing sales campaigns or other time-sensitive pages.', null=True, verbose_name='available to')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('modified_on', models.DateTimeField(auto_now=True, verbose_name='modified on')),
                ('identifier', shuup.core.fields.InternalIdentifierField(blank=True, editable=False, max_length=64, null=True, unique=True)),
                ('visible_in_menu', models.BooleanField(default=False, help_text='Check this if this page should have a link in the top menu of the store front.', verbose_name='visible in menu')),
                ('list_children_on_page', models.BooleanField(default=False, help_text='Check this if this page should list its children pages.', verbose_name='list children on page')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='modified by')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, help_text='Set this to a parent page if this page should be subcategorized under another page.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='shuup_simple_cms.Page', verbose_name='parent')),
            ],
            options={
                'ordering': ('-id',),
                'verbose_name': 'page',
                'verbose_name_plural': 'pages',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PageTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(help_text='The page title. This is shown anywhere links to your page are shown.', max_length=256, verbose_name='title')),
                ('url', models.CharField(blank=True, default=None, help_text='The page url. Choose a descriptive url so that search engines can rank your page higher. Often the best url is simply the page title with spaces replaced with dashes.', max_length=100, null=True, unique=True, verbose_name='URL')),
                ('content', models.TextField(help_text='The page content. This is the text that is displayed when customers click on your page link.', verbose_name='content')),
                ('master', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='shuup_simple_cms.Page')),
            ],
            options={
                'managed': True,
                'db_table': 'shuup_simple_cms_page_translation',
                'db_tablespace': '',
                'default_permissions': (),
                'verbose_name': 'page Translation',
            },
        ),
        migrations.AlterUniqueTogether(
            name='pagetranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]