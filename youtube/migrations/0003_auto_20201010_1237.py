# Generated by Django 3.1.2 on 2020-10-10 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0002_auto_20201010_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='path',
            field=models.FileField(upload_to='videos/'),
        ),
    ]
