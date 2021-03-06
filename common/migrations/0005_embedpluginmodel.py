# Generated by Django 3.1.12 on 2021-09-09 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('common', '0004_wrapperpluginmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmbedPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='common_embedpluginmodel', serialize=False, to='cms.cmsplugin')),
                ('content', models.TextField(blank=True, help_text='Put your HTML code here.', verbose_name='content')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
