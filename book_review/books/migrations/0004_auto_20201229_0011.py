# Generated by Django 3.1.4 on 2020-12-29 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20201228_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='review',
            field=models.TextField(max_length=6000),
        ),
    ]