# Generated by Django 3.2.6 on 2021-09-06 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='memberprofile',
            field=models.TextField(max_length=100, null=True, verbose_name='자기소개'),
        ),
    ]
