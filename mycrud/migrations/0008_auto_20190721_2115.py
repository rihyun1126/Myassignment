# Generated by Django 2.2.3 on 2019-07-21 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycrud', '0007_auto_20190721_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_user',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
