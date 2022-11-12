# Generated by Django 4.0.2 on 2022-02-16 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='button',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('button1', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_date', models.DateTimeField()),
                ('text', models.CharField(max_length=200)),
            ],
        ),
    ]
