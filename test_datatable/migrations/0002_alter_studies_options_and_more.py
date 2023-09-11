# Generated by Django 4.2.5 on 2023-09-09 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_datatable', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studies',
            options={'ordering': ['patient_fio', 'patient_birthdate', 'study_uid', 'study_date', 'study_modality']},
        ),
        migrations.AlterField(
            model_name='studies',
            name='patient_birthdate',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения пациента'),
        ),
    ]