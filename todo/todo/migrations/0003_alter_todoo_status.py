# Generated by Django 4.2.3 on 2023-07-28 03:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todo", "0002_alter_todoo_srno"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todoo",
            name="status",
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
