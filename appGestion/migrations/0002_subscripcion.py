# Generated by Django 4.2.2 on 2023-09-20 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appGestion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]
