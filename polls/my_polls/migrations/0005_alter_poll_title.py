# Generated by Django 3.2.3 on 2021-05-18 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_polls', '0004_auto_20210518_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
