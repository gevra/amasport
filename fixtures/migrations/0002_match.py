# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-26 10:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('club', '0002_auto_20161126_1015'),
        ('fixtures', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_start_time', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('host_score', models.IntegerField(blank=True, null=True)),
                ('guest_score', models.IntegerField(blank=True, null=True)),
                ('goal_scorers', models.TextField(blank=True)),
                ('status', models.CharField(blank=True, max_length=32)),
                ('guest', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='away', to='club.Club')),
                ('host', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home', to='club.Club')),
            ],
        ),
    ]
