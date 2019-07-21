# Generated by Django 2.2.3 on 2019-07-21 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mycrud', '0004_remove_comment_comment_thumbnail_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_user',
        ),
        migrations.AlterField(
            model_name='comment',
            name='blog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mycrud.Blog'),
        ),
    ]