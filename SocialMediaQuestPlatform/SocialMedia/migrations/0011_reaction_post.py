# Generated by Django 4.1.5 on 2023-03-02 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("SocialMedia", "0010_reaction"),
    ]

    operations = [
        migrations.AddField(
            model_name="reaction",
            name="post",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="SocialMedia.post",
            ),
        ),
    ]