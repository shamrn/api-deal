# Generated by Django 3.2.3 on 2021-05-19 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_filecsv_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='DealData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('spent_money', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
                ('gems', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='FileCsv',
        ),
    ]
