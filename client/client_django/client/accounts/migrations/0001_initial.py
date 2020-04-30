# Generated by Django 3.0.4 on 2020-03-12 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('sender_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='senderId')),
                ('receiver_id', models.IntegerField(verbose_name='receiverId')),
                ('state', models.IntegerField(verbose_name='stateCode')),
            ],
            options={
                'verbose_name': 'messageInfo',
                'verbose_name_plural': 'messageInfo',
            },
        ),
    ]
