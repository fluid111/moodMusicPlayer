# Generated by Django 5.1.1 on 2024-09-21 13:39

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Moods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('upload_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('type', models.CharField(choices=[('HA', 'HAPPY'), ('EX', 'EXCITED'), ('CA', 'CALM'), ('GR', 'GRATEFUL'), ('HO', 'HOPEFUL'), ('SA', 'SAD'), ('AN', 'ANGRY'), ('ANX', 'ANXIOUS'), ('BO', 'BORED'), ('LO', 'LONELY'), ('NI', 'INDIFFERENT'), ('PE', 'PENSIVE'), ('NO', 'NOSTALGIC'), ('BI', 'BITTERSWEET'), ('AM', 'AMBIVALENT'), ('RO', 'ROMANTIC'), ('PL', 'PLAYFUL'), ('ME', 'MELANCHOLIC'), ('MO', 'MOTIVATED')], max_length=3)),
            ],
        ),
    ]
