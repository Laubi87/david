# Generated by Django 3.2.4 on 2021-06-05 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='project',
            name='rank',
            field=models.IntegerField(default=0),
        ),
    ]
