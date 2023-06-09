# Generated by Django 3.2.18 on 2023-04-05 07:20

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0009_remove_image_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='description_shot',
            new_name='description_short',
        ),
        migrations.AlterField(
            model_name='image',
            name='order',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='Позиция'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(),
        ),
    ]
