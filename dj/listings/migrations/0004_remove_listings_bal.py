# Generated by Django 2.2.10 on 2020-07-06 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_listings_bal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listings',
            name='bal',
        ),
    ]
