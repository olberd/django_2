# Generated by Django 3.2.18 on 2023-03-28 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_auto_20230328_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
