# Generated by Django 4.1.3 on 2023-04-12 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("timetable", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="sem",
            name="department",
            field=models.CharField(default="it", max_length=255),
            preserve_default=False,
        ),
    ]
