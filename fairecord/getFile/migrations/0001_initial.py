# Generated by Django 3.2.9 on 2021-11-10 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.CharField(max_length=200)),
                ('down_date', models.DateTimeField(verbose_name='date downloaded')),
            ],
        ),
    ]
