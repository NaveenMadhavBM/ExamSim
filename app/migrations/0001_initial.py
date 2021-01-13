# Generated by Django 3.1.3 on 2020-12-11 19:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('date_Created', models.DateTimeField(auto_now_add=True, null=True)),
                ('Type', models.CharField(choices=[('Public', 'Public'), ('Private', 'Private')], max_length=50)),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Modules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.courses')),
            ],
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True, null=True)),
                ('marks', models.FloatField()),
                ('module', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.modules')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Q', models.CharField(max_length=1000)),
                ('opt1', models.CharField(max_length=200)),
                ('opt2', models.CharField(max_length=200)),
                ('opt3', models.CharField(blank=True, max_length=200, null=True)),
                ('opt4', models.CharField(blank=True, max_length=200, null=True)),
                ('marks', models.FloatField()),
                ('Correct', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=3)),
                ('Reason', models.CharField(blank=True, max_length=1000, null=True)),
                ('module', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.modules')),
            ],
        ),
        migrations.CreateModel(
            name='Answer_Sheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.FloatField()),
                ('Attempted_option', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=3)),
                ('Q', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.questions')),
                ('Result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.results')),
            ],
        ),
    ]
