# Generated by Django 4.2.4 on 2023-08-23 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='pub_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='reply',
            name='rep_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
