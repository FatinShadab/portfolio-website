# Generated by Django 5.1.3 on 2024-11-25 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalData', '0004_quickfact_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldata',
            name='short_bio',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]