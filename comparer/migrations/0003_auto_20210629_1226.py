# Generated by Django 3.1.12 on 2021-06-29 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comparer', '0002_rankingboxpluginmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='region',
            field=models.CharField(blank=True, max_length=100, verbose_name='region'),
        ),
        migrations.AddField(
            model_name='rankingboxpluginmodel',
            name='region_filter',
            field=models.CharField(blank=True, help_text='You can type more than one (separated with semicolon).', max_length=250, verbose_name='filter by regions'),
        ),
    ]
