# Generated by Django 4.1.3 on 2022-12-01 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='testDate',
            field=models.DateField(blank=True, help_text='검사일', null=True),
        ),
    ]
