# Generated by Django 2.2.6 on 2020-02-06 16:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('confma', '0010_auto_20200206_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloth',
            name='image',
            field=models.ImageField(default='notfound.jpg', upload_to='fashion'),
        ),
    ]
