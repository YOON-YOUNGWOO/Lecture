# Generated by Django 3.2.6 on 2021-09-24 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0012_auto_20210912_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='lecture_memo',
            field=models.TextField(default='강의 소개', max_length=100, null=True, verbose_name='강의 소개'),
        ),
        migrations.AddField(
            model_name='lecture',
            name='lecture_registrant',
            field=models.CharField(max_length=64, null=True, verbose_name='등록자'),
        ),
    ]
