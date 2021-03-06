# Generated by Django 3.0.8 on 2020-08-24 01:28

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datasource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fields', django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
                ('name', models.CharField(max_length=32)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='datasources', to='accounts.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.TextField()),
                ('name', models.CharField(max_length=32)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='templates', to='accounts.Account')),
                ('datasource', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='templates', to='emails.Datasource')),
                ('number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='templates', to='accounts.Number')),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
                ('name', models.CharField(max_length=32)),
                ('created', models.DateTimeField(auto_now=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emails', to='accounts.Account')),
                ('datasource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emails', to='emails.Datasource')),
            ],
        ),
    ]
