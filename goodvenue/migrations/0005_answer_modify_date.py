# Generated by Django 4.0.3 on 2022-12-22 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goodvenue', '0004_alter_answer_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]