# Generated by Django 4.2.2 on 2023-09-22 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appGestion', '0004_alter_subscripcion_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscripcion',
            name='nombre',
            field=models.CharField(default=True, max_length=50),
        ),
    ]
