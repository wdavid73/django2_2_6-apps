# Generated by Django 2.2.6 on 2019-10-13 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('confma', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]