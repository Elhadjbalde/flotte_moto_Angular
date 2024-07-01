# Generated by Django 5.0.6 on 2024-06-13 20:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chauffeurs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Moto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_serie', models.CharField(max_length=50, unique=True)),
                ('color', models.CharField(max_length=50)),
                ('date_achat', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
                ('chauffeur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='chauffeurs.chauffeur')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='moto_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='moto_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]