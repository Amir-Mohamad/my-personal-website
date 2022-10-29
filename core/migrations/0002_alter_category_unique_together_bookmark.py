# Generated by Django 4.1.1 on 2022-10-29 20:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("contenttypes", "0002_remove_content_type_name"),
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="category",
            unique_together={("slug", "parent")},
        ),
        migrations.CreateModel(
            name="Bookmark",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("updated", models.DateTimeField(auto_now_add=True)),
                ("created", models.DateTimeField(auto_now=True)),
                ("is_active", models.BooleanField(default=False)),
                ("parent_object_id", models.IntegerField(default=1)),
                (
                    "parent_content_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="contenttypes.contenttype",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bookmarks",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]