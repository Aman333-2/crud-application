# Generated by Django 4.0.4 on 2022-07-18 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=78)),
                ('email', models.CharField(max_length=58)),
                ('password', models.CharField(max_length=65)),
            ],
        ),
    ]
