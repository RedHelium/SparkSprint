# Generated by Django 5.0.6 on 2024-06-17 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskcolumn',
            name='max_task',
            field=models.IntegerField(blank=True, null=True, verbose_name='Макс. кол-во задач'),
        ),
    ]