# Generated by Django 4.2.4 on 2023-08-09 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_create_pet'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
