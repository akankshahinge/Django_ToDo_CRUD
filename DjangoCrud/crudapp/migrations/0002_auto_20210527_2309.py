# Generated by Django 3.1 on 2021-05-28 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
