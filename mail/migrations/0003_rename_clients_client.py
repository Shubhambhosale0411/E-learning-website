# Generated by Django 4.0 on 2022-01-02 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0002_alter_clients_date_created_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Clients',
            new_name='Client',
        ),
    ]
