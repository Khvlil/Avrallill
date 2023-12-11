# Generated by Django 4.2.7 on 2023-11-20 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_overview', models.CharField(max_length=1000)),
                ('research_and_inspiration', models.CharField(max_length=1000)),
                ('problem_statement', models.CharField(max_length=1000)),
                ('concept_and_design_principles', models.CharField(max_length=1000)),
                ('challenges_and_solutions', models.CharField(max_length=1000)),
                ('conclusion_and_next_steps', models.CharField(max_length=1000)),
                ('project_date_created', models.DateField()),
                ('github_link', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designs', models.FileField(upload_to='Designs')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.post')),
            ],
        ),
    ]
