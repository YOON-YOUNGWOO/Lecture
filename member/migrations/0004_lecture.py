# Generated by Django 3.2.6 on 2021-09-07 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_alter_member_memberprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('lectureid', models.AutoField(primary_key=True, serialize=False)),
                ('lectureName', models.CharField(max_length=64, verbose_name='강의이름')),
                ('lectureregistered', models.DateTimeField(auto_now_add=True, verbose_name='등록 일자')),
            ],
        ),
    ]