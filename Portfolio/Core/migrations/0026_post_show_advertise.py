# Generated by Django 4.2.7 on 2023-11-26 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0025_post_project_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='show_advertise',
            field=models.BooleanField(default=False),
        ),
    ]