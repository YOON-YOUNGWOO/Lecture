# Generated by Django 3.2.6 on 2021-09-07 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0004_lecture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member_Lecture',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('lecture_id', models.ForeignKey(db_column='lecture_id', on_delete=django.db.models.deletion.CASCADE, related_name='lecture', to='member.lecture')),
                ('member_id', models.ForeignKey(db_column='member_id', on_delete=django.db.models.deletion.CASCADE, related_name='member', to='member.member')),
            ],
        ),
    ]
