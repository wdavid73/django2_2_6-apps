# Generated by Django 2.2.6 on 2020-02-06 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('confma', '0004_cloth_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cloth',
            name='photo',
        ),
    ]