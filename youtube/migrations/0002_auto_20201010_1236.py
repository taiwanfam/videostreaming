# Generated by Django 3.1.2 on 2020-10-10 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='description',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]
