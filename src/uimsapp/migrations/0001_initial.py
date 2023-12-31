# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uimsapp.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BudgetEntity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('budget_entity', models.CharField(default=b'', max_length=200, null=True, blank=True)),
                ('positionNameOne', models.CharField(default=b'', max_length=120, null=True, blank=True)),
                ('gradeOne', models.CharField(default=b'', max_length=120, null=True, blank=True)),
                ('quantityOne', models.IntegerField(null=True, blank=True)),
                ('ocupiedOne', models.IntegerField(null=True, blank=True)),
                ('vacantOne', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('passport_picture', models.FileField(null=True, upload_to=uimsapp.models.upload_location, blank=True)),
                ('employment_number', models.CharField(default=b'', max_length=120, null=True, blank=True)),
                ('title', models.CharField(default=b'', max_length=120, null=True, blank=True)),
                ('name', models.CharField(default=b'', max_length=120, null=True, blank=True)),
                ('nationality', models.CharField(default=b'', max_length=120, null=True, blank=True)),
                ('id_card_number', models.CharField(default=b'', max_length=120, null=True, blank=True)),
                ('home_country', models.CharField(default=b'', max_length=120, null=True, blank=True)),
                ('residence', models.CharField(default=b'', max_length=120, null=True, blank=True)),
                ('contact_number', models.CharField(default=b'', max_length=120, null=True, blank=True)),
                ('email_address', models.CharField(default=b'', max_length=120, null=True, blank=True)),
                ('status', models.CharField(default=b'', max_length=120, null=True, blank=True)),
                ('status_start_date', models.DateField(null=True, verbose_name=b'Status Start Date', blank=True)),
                ('status_end_date', models.DateField(null=True, verbose_name=b'Status End Date', blank=True)),
                ('vocation_start_date', models.DateField(null=True, verbose_name=b'Vocation Start Date', blank=True)),
                ('vocation_end_date', models.DateField(null=True, verbose_name=b'Vocation End Date', blank=True)),
                ('alert_days', models.IntegerField(null=True, verbose_name=b'Alert when status due in Days', blank=True)),
                ('dob', models.DateField(null=True, verbose_name=b'Date of Birth', blank=True)),
                ('place_of_birth', models.CharField(default=b'', max_length=120, null=True, blank=True)),
                ('fad', models.DateField(null=True, verbose_name=b'First Appointment Date', blank=True)),
                ('cad', models.DateField(null=True, verbose_name=b'Current Appointment Date', blank=True)),
                ('cd', models.DateField(null=True, verbose_name=b'Confirmed Date', blank=True)),
                ('graduation_year', models.DateField(null=True, blank=True)),
                ('designation', models.CharField(default=b'', max_length=120, null=True, blank=True)),
                ('division', models.CharField(blank=True, max_length=50, null=True, verbose_name=b'Region', choices=[(b'Greater Banjul, region one', b'Greater Banjul, region one'), (b'West coast Region, region two', b'West coast Region, region two'), (b'North Bank Region, region three', b'North Bank Region, region three'), (b'Lower River Region, region four', b'North Bank Region, region four'), (b'Central River Region, region five', b'Central River Region, region five'), (b'Upper River Region, region six', b'Central River Region, region six')])),
                ('duty_station', models.CharField(default=b'', max_length=120, null=True, blank=True)),
                ('grade', models.IntegerField(null=True, blank=True)),
                ('grade_point', models.IntegerField(null=True, blank=True)),
                ('next_of_kin', models.CharField(default=b'', max_length=120, null=True, blank=True)),
                ('qualification', models.TextField(default=b'', max_length=300, null=True, verbose_name=b'Educational Background', blank=True)),
                ('tin_number', models.CharField(default=b'', max_length=120, null=True, blank=True)),
                ('added_by', models.CharField(default=b'', max_length=120, null=True, blank=True)),
                ('updated_by', models.CharField(default=b'', max_length=120, null=True, blank=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('date_of_retirement', models.CharField(max_length=30, null=True, blank=True)),
                ('School_of_graduation', models.CharField(max_length=30, null=True, blank=True)),
                ('marital_status', models.CharField(blank=True, max_length=30, null=True, choices=[(b'Married', b'Married'), (b'Single', b'Single')])),
                ('gender', models.CharField(blank=True, max_length=30, null=True, choices=[(b'Male', b'Male'), (b'Female', b'Female')])),
                ('highest_qualification', models.CharField(blank=True, max_length=50, null=True, choices=[(b'None', b'None'), (b'Arabic', b'Arabic'), (b'Primary School', b'Primary School'), (b'Upper Basic', b'Upper Basic'), (b'Senior Secondary School', b'Senior Secondary School'), (b'CAT', b'CAT'), (b'AAT', b'AAT'), (b'ACCA', b'ACCA'), (b'ECD', b'ECD'), (b'PTC', b'PTC'), (b'HTC', b'HTC'), (b'Other Professional Qualification', b'Other Professional Qualification'), (b'Bachelors Degree', b'Bachelors Degree'), (b'Bachelors/Masters Degree', b'Bachelors/Massters Degree'), (b'Bachelors Degree/ACCA', b'Bachelors Degree/ACCA'), (b'Masters Degree', b'Masters Degree'), (b'Masters Degree/ACCA', b'Masters Degree/ACCA'), (b'Bachelors/Masters Degree/ACCA', b'Bachelors/Masters Degree/ACCA'), (b'Professional/Bachelors Degree', b'Professional/Bachelors Degree'), (b'Professional/Masters Degree', b'Professional/Masters Degree'), (b'Professional/Bachelors/Masters Degree', b'Professional/Bachelors/Masters Degree')])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('budget_entity', models.ForeignKey(blank=True, to='uimsapp.BudgetEntity', null=True)),
            ],
            options={
                'db_table': 'uimsapp_employee',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EmployeeAudit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('passport_picture', models.FileField(null=True, upload_to=uimsapp.models.upload_location, blank=True)),
                ('employment_number', models.CharField(default=b'', max_length=120, null=True, blank=True)),
                ('title', models.CharField(default=b'', max_length=120, null=True, blank=True)),
                ('name', models.CharField(default=b'', max_length=120, null=True, blank=True)),
                ('gender', models.CharField(default=b'', max_length=120, null=True, blank=True)),
                ('nationality', models.CharField(default=b'', max_length=120, null=True, blank=True)),
                ('id_card_number', models.CharField(default=b'', max_length=120, null=True, blank=True)),
                ('home_country', models.CharField(default=b'', max_length=120, null=True, blank=True)),
                ('residence', models.CharField(default=b'', max_length=120, null=True, blank=True)),
                ('contact_number', models.CharField(default=b'', max_length=120, null=True, blank=True)),
                ('email_address', models.CharField(default=b'', max_length=120, null=True, blank=True)),
                ('status', models.CharField(default=b'', max_length=120, null=True, blank=True)),
                ('status_start_date', models.DateField(null=True, verbose_name=b'Status Start Date', blank=True)),
                ('status_end_date', models.DateField(null=True, verbose_name=b'Status End Date', blank=True)),
                ('vocation_start_date', models.DateField(null=True, verbose_name=b'Vocation Start Date', blank=True)),
                ('vocation_end_date', models.DateField(null=True, verbose_name=b'Vocation End Date', blank=True)),
                ('alert_days', models.IntegerField(null=True, verbose_name=b'Alert when status due in Days', blank=True)),
                ('dob', models.DateField(null=True, verbose_name=b'Date of Birth', blank=True)),
                ('place_of_birth', models.CharField(default=b'', max_length=120, null=True, blank=True)),
                ('fad', models.DateField(null=True, verbose_name=b'First Appointment Date', blank=True)),
                ('cad', models.DateField(null=True, verbose_name=b'Current Appointment Date', blank=True)),
                ('cd', models.DateField(null=True, verbose_name=b'Confirmed Date', blank=True)),
                ('designation', models.CharField(default=b'', max_length=120, null=True, blank=True)),
                ('division', models.CharField(default=b'', max_length=120, null=True, blank=True)),
                ('duty_station', models.CharField(default=b'', max_length=120, null=True, blank=True)),
                ('grade', models.IntegerField(null=True, blank=True)),
                ('grade_point', models.IntegerField(null=True, blank=True)),
                ('next_of_kin', models.CharField(default=b'', max_length=120, null=True, blank=True)),
                ('qualification', models.TextField(default=b'', max_length=3000, null=True, blank=True)),
                ('tin_number', models.CharField(default=b'', max_length=120, null=True, blank=True)),
                ('marital_status', models.CharField(default=b'', max_length=120, null=True, blank=True)),
                ('added_by', models.CharField(default=b'', max_length=120, null=True, blank=True)),
                ('updated_by', models.CharField(default=b'', max_length=120, null=True, blank=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('budget_entity', models.ForeignKey(blank=True, to='uimsapp.BudgetEntity', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('birth_date', models.DateField()),
                ('location', models.CharField(max_length=100, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('employment_number', models.CharField(default=b'', max_length=120, null=True, blank=True)),
                ('name', models.CharField(default=b'', max_length=120, null=True, blank=True)),
                ('gender', models.CharField(default=b'', max_length=120, null=True, blank=True)),
                ('status', models.CharField(default=b'', max_length=120, null=True, blank=True)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('last_updated_from', models.DateField(null=True, blank=True)),
                ('last_updated_to', models.DateField(null=True, verbose_name=b'To', blank=True)),
                ('export_to_CSV', models.BooleanField(default=False)),
                ('budget_entity', models.ForeignKey(blank=True, to='uimsapp.BudgetEntity', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vocation', models.CharField(default=b'', max_length=200, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='employeeaudit',
            name='vocation',
            field=models.ForeignKey(blank=True, to='uimsapp.Vocation', null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='vocation',
            field=models.ForeignKey(blank=True, to='uimsapp.Vocation', null=True),
        ),
    ]
