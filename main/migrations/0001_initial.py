# Generated by Django 4.1.3 on 2022-11-30 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('number', models.IntegerField(help_text='질문번호', primary_key=True, serialize=False)),
                ('content', models.CharField(blank=True, help_text='질문내용', max_length=100, null=True)),
                ('test_column', models.IntegerField(choices=[(0, '신체'), (1, '인지'), (2, '언어'), (3, '정서'), (4, '사회성'), (5, '자폐'), (6, 'Adhd')], help_text='규준표 컬럼')),
                ('group', models.IntegerField(choices=[(0, 'A'), (1, 'B'), (2, 'C')], help_text='질문그룹')),
            ],
        ),
    ]
