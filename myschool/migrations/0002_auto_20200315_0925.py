# Generated by Django 2.0 on 2020-03-15 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myschool', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='classroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_cls', to='myschool.Classroom'),
        ),
    ]
