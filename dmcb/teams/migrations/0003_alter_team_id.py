# Generated by Django 4.0.5 on 2022-07-06 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_participant_team_delete_question_participant_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
