# Generated by Django 3.2.3 on 2022-09-24 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_alter_bece_schooltype_alter_bece_startingdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bece',
            old_name='RequestId',
            new_name='schoolIds',
        ),
    ]
