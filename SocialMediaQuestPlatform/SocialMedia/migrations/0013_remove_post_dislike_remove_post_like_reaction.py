# Generated by Django 4.1.5 on 2023-03-02 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("SocialMedia", "0012_post_dislike_post_like_delete_reaction"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="dislike",
        ),
        migrations.RemoveField(
            model_name="post",
            name="like",
        ),
        migrations.CreateModel(
            name="Reaction",
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
                ("like", models.BooleanField(default=False)),
                ("dislike", models.BooleanField(default=False)),
                (
                    "post",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="SocialMedia.post",
                    ),
                ),
            ],
        ),
    ]
