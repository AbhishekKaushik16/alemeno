# Generated by Django 4.0 on 2021-12-23 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("alemeno", "0003_remove_image_image_url_image_image_field"),
    ]

    operations = [
        migrations.RenameField(
            model_name="image",
            old_name="image_field",
            new_name="image",
        ),
    ]