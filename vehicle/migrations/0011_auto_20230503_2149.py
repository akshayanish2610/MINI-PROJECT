# Generated by Django 3.0.5 on 2023-05-03 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0010_auto_20230430_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='category',
            field=models.CharField(choices=[('two wheeler with gear', 'two wheeler with gear'), ('two wheeler without gear', 'two wheeler without gear'), ('four wheeler', 'four wheeler')], max_length=50),
        ),
    ]
