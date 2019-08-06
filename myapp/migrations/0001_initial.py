# Generated by Django 2.2.3 on 2019-08-02 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pms_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_id', models.CharField(max_length=20)),
                ('ram_usage', models.CharField(max_length=20)),
                ('cpu_usage', models.CharField(max_length=20)),
                ('mac_address', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=10)),
                ('date_time', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='pms_db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=20, unique=True)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]