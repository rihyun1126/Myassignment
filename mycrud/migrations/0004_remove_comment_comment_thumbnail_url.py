# Generated by Django 2.2.3 on 2019-07-21 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mycrud', '0003_auto_20190721_0637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_thumbnail_url',
        ),
    ]
