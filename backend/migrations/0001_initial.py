# Generated by Django 4.1.1 on 2022-09-23 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=50, null=True)),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('difficulty', models.CharField(blank=True, max_length=100, null=True)),
                ('question', models.CharField(blank=True, max_length=500, null=True)),
                ('correct', models.CharField(blank=True, max_length=50, null=True)),
                ('wrong', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
