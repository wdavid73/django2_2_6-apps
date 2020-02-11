# Generated by Django 2.2.6 on 2020-02-06 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('confma', '0002_remove_client_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='static/fashion/notfound.jpg', upload_to='static/fashion')),
                ('name', models.CharField(max_length=200)),
                ('state', models.SmallIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]