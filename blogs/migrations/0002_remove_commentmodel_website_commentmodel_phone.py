# Generated by Django 4.1.5 on 2023-01-09 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentmodel',
            name='website',
        ),
        migrations.AddField(
            model_name='commentmodel',
            name='phone',
            field=models.CharField(default=None, max_length=13, verbose_name='phone'),
            preserve_default=False,
        ),
    ]