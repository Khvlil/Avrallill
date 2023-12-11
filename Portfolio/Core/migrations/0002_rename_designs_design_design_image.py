# Generated by Django 4.2.7 on 2023-11-20 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='design',
            old_name='designs',
            new_name='design',
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='Designs')),
                ('design', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.design')),
            ],
        ),
    ]
