# Generated by Django 2.1 on 2018-09-05 11:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0002_delete_questionmanager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='likes',
            field=models.ManyToManyField(null=True, related_name='likes_set', to=settings.AUTH_USER_MODEL),
        ),
    ]
