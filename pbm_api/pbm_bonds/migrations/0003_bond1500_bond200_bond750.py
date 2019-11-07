# Generated by Django 2.2.5 on 2019-11-07 10:32

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pbm_bonds', '0002_bonddrawdates'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bond750',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=0, help_text='Year of prize bond announced')),
                ('date', models.DateField(default=datetime.date.today)),
                ('bond_number', models.IntegerField(default=0, help_text='Prize bond number')),
                ('bond_level', models.IntegerField(choices=[(1, 'First'), (2, 'Second'), (3, 'Third')])),
                ('bond_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pbm_bonds.BondCategory')),
            ],
        ),
        migrations.CreateModel(
            name='Bond200',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=0, help_text='Year of prize bond announced')),
                ('date', models.DateField(default=datetime.date.today)),
                ('bond_number', models.IntegerField(default=0, help_text='Prize bond number')),
                ('bond_level', models.IntegerField(choices=[(1, 'First'), (2, 'Second'), (3, 'Third')])),
                ('bond_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pbm_bonds.BondCategory')),
            ],
        ),
        migrations.CreateModel(
            name='Bond1500',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=0, help_text='Year of prize bond announced')),
                ('date', models.DateField(default=datetime.date.today)),
                ('bond_number', models.IntegerField(default=0, help_text='Prize bond number')),
                ('bond_level', models.IntegerField(choices=[(1, 'First'), (2, 'Second'), (3, 'Third')])),
                ('bond_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pbm_bonds.BondCategory')),
            ],
        ),
    ]
