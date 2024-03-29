# Generated by Django 3.0.5 on 2021-02-21 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosmicsns', '0004_auto_20210221_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nick_name',
            field=models.CharField(default=999, max_length=50, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
