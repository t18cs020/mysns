# Generated by Django 3.0.5 on 2021-02-21 11:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cosmicsns', '0011_auto_20210221_1953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='departments',
        ),
        migrations.RemoveField(
            model_name='user',
            name='followers',
        ),
        migrations.RemoveField(
            model_name='user',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='introduction',
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
        migrations.AlterField(
            model_name='user',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='profiles/'),
        ),
        migrations.DeleteModel(
            name='Department',
        ),
    ]
