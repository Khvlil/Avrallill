# Generated by Django 4.2.7 on 2023-11-21 17:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0007_post_project_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='design',
            old_name='project',
            new_name='design',
        ),
        migrations.RemoveField(
            model_name='design',
            name='designs',
        ),
        migrations.AddField(
            model_name='design',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='Design'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]