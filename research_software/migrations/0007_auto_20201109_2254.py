# Generated by Django 2.2 on 2020-11-09 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research_software', '0006_auto_20201109_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tileobject',
            name='Status',
            field=models.CharField(choices=[('live', 'Live'), ('pending', 'Pending'), ('archived', 'Archived')], default='pen', max_length=10),
        ),
    ]
