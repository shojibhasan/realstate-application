# Generated by Django 2.2.10 on 2020-07-06 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realtos', '0005_realtor_is_mvp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='realtor',
            name='is_mvp',
        ),
    ]
