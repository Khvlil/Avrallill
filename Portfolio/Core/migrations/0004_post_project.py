# Generated by Django 4.2.7 on 2023-11-20 18:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0003_remove_design_design_design_designs_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='project',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]