# Generated by Django 4.1.1 on 2022-09-16 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=16)),
                ('senha', models.CharField(max_length=16)),
                ('nome', models.CharField(max_length=16)),
                ('ultimo_nome', models.CharField(max_length=16)),
            ],
        ),
    ]
