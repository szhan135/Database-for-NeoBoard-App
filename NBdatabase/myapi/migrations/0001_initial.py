# Generated by Django 2.2.12 on 2020-08-12 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('userId', models.IntegerField()),
            ],
        ),
    ]
