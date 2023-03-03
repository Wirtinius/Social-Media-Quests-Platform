# Generated by Django 4.1.5 on 2023-03-03 06:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("SocialMedia", "0014_alter_reaction_post"),
    ]

    operations = [
        migrations.AddField(
            model_name="reaction",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]