# Generated by Django 3.1.4 on 2020-12-29 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='https://www.pressgazette.co.uk/wp-content/uploads/2020/11/shutterstock.jpg', upload_to='blog/images/'),
        ),
    ]
