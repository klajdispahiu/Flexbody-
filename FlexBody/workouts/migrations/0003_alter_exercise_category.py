# Generated by Django 5.0.3 on 2024-04-05 15:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0002_remove_exercise_unique_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='workouts.category'),
        ),
    ]
