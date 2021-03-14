# Generated by Django 3.1.6 on 2021-02-24 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Corporation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('logo', models.URLField()),
                ('description', models.TextField(max_length=1863)),
                ('url_id', models.CharField(max_length=15)),
            ],
        ),
    ]
