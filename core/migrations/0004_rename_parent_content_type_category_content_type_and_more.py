# Generated by Django 4.1.1 on 2022-10-15 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_alter_category_options"),
    ]

    operations = [
        migrations.RenameField(
            model_name="category",
            old_name="parent_content_type",
            new_name="content_type",
        ),
        migrations.RenameField(
            model_name="category",
            old_name="parent_object_id",
            new_name="object_id",
        ),
    ]
