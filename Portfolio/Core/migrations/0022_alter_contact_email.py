# Generated by Django 4.2.7 on 2023-11-24 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0021_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(max_length=50),
        ),
    ]
