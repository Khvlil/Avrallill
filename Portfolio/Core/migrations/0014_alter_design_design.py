# Generated by Django 4.2.7 on 2023-11-23 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0013_alter_design_design'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design',
            name='design',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='design', to='Core.post'),
        ),
    ]
