# Generated by Django 4.2.7 on 2023-11-28 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chat_Bot', '0003_auto_20231128_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='mobile_number',
        ),
        migrations.AddField(
            model_name='signup',
            name='phone_number',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='signup',
            name='full_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='signup',
            name='password',
            field=models.CharField(max_length=255),
        ),
    ]