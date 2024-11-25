# Generated by Django 5.1.3 on 2024-11-25 10:35

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AwardsAndRecognition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Biography',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='EducationalBackground',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program', models.CharField(max_length=100)),
                ('provider', models.CharField(max_length=100)),
                ('provider_link', models.URLField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Current', 'Current'), ('Completed', 'Completed')], default='Completed', max_length=10)),
                ('result', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='personalData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='profile/')),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='ProfessionalExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100)),
                ('organization', models.CharField(max_length=100)),
                ('organization_link', models.URLField(blank=True, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('at_present', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('publication_body', models.CharField(max_length=100)),
                ('link', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ResearchInterest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Facebook', 'Facebook'), ('Twitter', 'Twitter'), ('LinkedIn', 'LinkedIn'), ('Instagram', 'Instagram'), ('GitHub', 'GitHub'), ('GitLab', 'GitLab'), ('Bitbucket', 'Bitbucket'), ('StackOverflow', 'StackOverflow'), ('ResearchGate', 'ResearchGate'), ('GoogleScholar', 'GoogleScholar'), ('PersonalWebsite', 'PersonalWebsite')], max_length=100)),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='TechnicalProtfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
    ]
