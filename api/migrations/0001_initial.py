# Generated by Django 4.2.11 on 2024-04-22 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('login', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('age_label', models.CharField(choices=[('12-15', '12-15'), ('16-19', '16-19'), ('20 va undan yuqori', '20 va undan yuqori')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_type', models.CharField(choices=[('Elementary', 'Elementary'), ('Arifmetik', 'Arifmetik'), ('Professional', 'Professional')], max_length=50)),
                ('question_label', models.ManyToManyField(to='api.user')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_value', models.IntegerField()),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(auto_now_add=True)),
                ('result_label', models.ManyToManyField(to='api.user')),
            ],
        ),
    ]
