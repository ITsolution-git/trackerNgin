# Generated by Django 3.2 on 2021-04-24 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TrackerProxy', '0002_alter_users_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='Verification_code',
            new_name='Verification_Code',
        ),
    ]
