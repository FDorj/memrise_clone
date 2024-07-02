# Generated by Django 5.0.6 on 2024-06-29 10:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('exercises', models.ManyToManyField(related_name='lessons', to='group2.exercise')),
            ],
        ),
        migrations.CreateModel(
            name='LessonCompletion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completion_date', models.DateTimeField(auto_now_add=True)),
                ('score', models.IntegerField()),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group2.lesson')),
            ],
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scores', models.JSONField(default=dict)),
                ('completed_lessons', models.ManyToManyField(related_name='completed_by', through='group2.LessonCompletion', to='group2.lesson')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='progress', to='group2.user')),
            ],
        ),
        migrations.AddField(
            model_name='lessoncompletion',
            name='progress',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='group2.progress'),
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.CharField(max_length=200)),
                ('results', models.ManyToManyField(to='group2.lesson')),
            ],
        ),
        migrations.AddField(
            model_name='lessoncompletion',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group2.user'),
        ),
    ]