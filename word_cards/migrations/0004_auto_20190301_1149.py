# Generated by Django 2.1 on 2019-03-01 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word_cards', '0003_auto_20190227_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='words',
            name='en_word',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='words',
            name='ua_word',
            field=models.CharField(max_length=16),
        ),
    ]
