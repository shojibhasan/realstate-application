# Generated by Django 2.2.10 on 2020-07-06 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realtos', '0002_realtor_is_mvp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='realtor',
            old_name='is_mvp',
            new_name='mvp_is',
        ),
    ]
