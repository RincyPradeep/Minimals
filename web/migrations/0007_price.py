# Generated by Django 4.0.2 on 2022-02-04 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_help'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=128)),
                ('title', models.CharField(choices=[('1', 'Standard'), ('2', 'Standard Plus'), ('3', 'Extended')], max_length=128)),
                ('one_end_products', models.BooleanField(default=False)),
                ('_12_months_updates', models.BooleanField(default=False)),
                ('_6_months_of_support', models.BooleanField(default=False)),
                ('javascript_version', models.BooleanField(default=False)),
                ('typescript_version', models.BooleanField(default=False)),
                ('design_resources', models.BooleanField(default=False)),
                ('commercial_applications', models.BooleanField(default=False)),
            ],
        ),
    ]