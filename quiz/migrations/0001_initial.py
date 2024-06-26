# Generated by Django 5.0.1 on 2024-04-15 19:34

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('uuid', models.UUIDField(default=uuid.UUID('459e1c0a-ab87-44a3-b59c-11a1daed987a'), editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('category_name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('uuid', models.UUIDField(default=uuid.UUID('459e1c0a-ab87-44a3-b59c-11a1daed987a'), editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('options', models.CharField(max_length=100)),
                ('marks', models.IntegerField(default=5)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('uuid', models.UUIDField(default=uuid.UUID('459e1c0a-ab87-44a3-b59c-11a1daed987a'), editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('answer', models.CharField(max_length=100)),
                ('is_correct', models.BooleanField(default=False)),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_answer', to='quiz.question')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
