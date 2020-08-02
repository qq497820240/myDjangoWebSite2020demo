# Generated by Django 2.2.1 on 2020-02-18 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('train_pic', '0006_auto_20200218_0330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Web_Range',
            fields=[
                ('Wid', models.AutoField(primary_key=True, serialize=False)),
                ('WRanName', models.CharField(default='null', max_length=100, unique=True)),
                ('WRanNum', models.IntegerField(default=0)),
                ('WRanPath', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Web_pic',
            fields=[
                ('Wid', models.AutoField(primary_key=True, serialize=False)),
                ('Wpic', models.ImageField(default='null', upload_to='img')),
                ('WpicRange', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='train_pic.Web_Range', to_field='WRanName')),
            ],
        ),
    ]
