# Generated by Django 4.0 on 2021-12-20 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("alemeno", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="created_on",
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="image",
            name="updated_on",
            field=models.DateTimeField(),
        ),
    ]