# Generated by Django 2.2.16 on 2020-11-01 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]