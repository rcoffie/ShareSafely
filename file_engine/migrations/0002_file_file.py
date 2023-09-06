# Generated by Django 4.2 on 2023-09-06 12:35

from django.db import migrations, models
import file_engine.validators


class Migration(migrations.Migration):
    dependencies = [
        ("file_engine", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="file",
            name="file",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="documents/%Y/%m/%d",
                validators=[file_engine.validators.validate_file_extension],
            ),
        ),
    ]