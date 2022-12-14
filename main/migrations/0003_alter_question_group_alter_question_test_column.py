# Generated by Django 4.1.3 on 2022-11-30 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_question_group_alter_question_test_column'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='group',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], help_text='질문그룹', max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='test_column',
            field=models.CharField(blank=True, choices=[('body', '신체'), ('recognition', '인지'), ('language', '언어'), ('emotion', '정서'), ('sociality', '사회성'), ('autism', '자폐경향성'), ('adhd', 'ADHD경향성')], help_text='규준표 컬럼', max_length=11, null=True),
        ),
    ]
