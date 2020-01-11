# Generated by Django 2.2 on 2020-01-10 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_sitkh'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruit',
            name='living_planet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.Planet', verbose_name='Планета обитания'),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recruit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Recruit')),
                ('sitkh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Sitkh')),
            ],
        ),
    ]
