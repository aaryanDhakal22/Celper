# Generated by Django 4.1.2 on 2022-10-20 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("celtick", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Tickets",
            new_name="Ticket",
        ),
    ]
