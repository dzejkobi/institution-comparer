# Generated by Django 3.1.12 on 2021-09-14 14:01

from django.db import migrations
import djangocms_bootstrap4.fields


class Migration(migrations.Migration):

    dependencies = [
        ('comparer', '0020_auto_20210831_1144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rankingboxpluginmodel',
            name='html_classes',
        ),
        migrations.AddField(
            model_name='rankingboxpluginmodel',
            name='attributes',
            field=djangocms_bootstrap4.fields.AttributesField(blank=True, default=dict, verbose_name='attributes'),
        ),
        migrations.AddField(
            model_name='rankingboxpluginmodel',
            name='tag_type',
            field=djangocms_bootstrap4.fields.TagTypeField(choices=[('div', 'div'), ('section', 'section'), ('article', 'article'), ('header', 'header'), ('footer', 'footer'), ('aside', 'aside')], default='div', help_text='Select the HTML tag to be used.', max_length=255, verbose_name='Tag type'),
        ),
    ]
