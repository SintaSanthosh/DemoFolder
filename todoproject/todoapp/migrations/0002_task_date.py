# Generated by Django 4.2.5 on 2023-10-16 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2001-03-30'),
            preserve_default=False,
        ),
    ]
