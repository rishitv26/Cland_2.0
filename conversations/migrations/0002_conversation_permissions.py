# Generated by Django 3.1.7 on 2021-03-20 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation_permissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_link', models.BooleanField(default=False)),
                ('is_particapant_permission', models.BooleanField(default=False)),
                ('conversation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conversations.conversation')),
            ],
        ),
    ]