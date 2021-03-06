# Generated by Django 4.0.1 on 2022-02-04 17:22

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
            name='Taskai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diena', models.DateField()),
                ('pristatymai', models.IntegerField()),
                ('pristatymai_pakuotes', models.IntegerField(blank=True, null=True)),
                ('uzsakymai', models.IntegerField()),
                ('uzsakymai_pakuotes', models.IntegerField(blank=True, null=True)),
                ('nepavyko', models.CharField(max_length=50)),
                ('km', models.IntegerField()),
                ('arbata', models.CharField(blank=True, max_length=50, null=True)),
                ('apie', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['diena'],
            },
        ),
    ]
