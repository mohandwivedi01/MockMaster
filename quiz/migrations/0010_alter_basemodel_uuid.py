# Generated by Django 5.0.1 on 2024-05-09 10:48

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_alter_basemodel_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basemodel',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('95cc65f2-adac-4b51-8ac4-fb9aadaf97ba'), editable=False, primary_key=True, serialize=False),
        ),
    ]
