# Generated by Django 2.2.1 on 2020-02-18 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('train_pic', '0005_auto_20200217_0836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='web_text',
            name='Wpic',
        ),
        migrations.RemoveField(
            model_name='web_text',
            name='WpicName',
        ),
    ]
