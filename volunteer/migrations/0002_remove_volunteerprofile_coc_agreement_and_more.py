# Generated by Django 5.1.7 on 2025-03-23 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("volunteer", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="volunteerprofile",
            name="coc_agreement",
        ),
        migrations.RemoveField(
            model_name="volunteerprofile",
            name="pronouns",
        ),
    ]
