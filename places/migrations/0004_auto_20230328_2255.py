# Generated by Django 3.2.18 on 2023-03-28 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_rename_images_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='link',
            new_name='place',
        ),
        migrations.AddField(
            model_name='image',
            name='url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
