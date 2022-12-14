# Generated by Django 4.1.3 on 2022-12-06 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_incheonregion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='residence',
            field=models.ForeignKey(blank=True, help_text='거주지역', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='residence', to='user.incheonregion'),
        ),
        migrations.AlterField(
            model_name='child',
            name='tester',
            field=models.ForeignKey(blank=True, help_text='검사자', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tester', to='user.tester'),
        ),
    ]
