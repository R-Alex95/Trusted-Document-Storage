# Generated by Django 3.0.4 on 2020-03-18 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_uploadfile_filepath'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='nrr',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='nrr'),
        ),
    ]