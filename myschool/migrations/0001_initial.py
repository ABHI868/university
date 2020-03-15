# Generated by Django 2.0 on 2020-03-15 08:10

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('seating_capacity', models.IntegerField()),
                ('shape', models.CharField(choices=[('Oval', 'Oval'), ('rectangular', 'rectangular'), ('canopy', 'canopy'), ('elevated', 'elevated')], max_length=12)),
                ('web_support', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Relatives',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_no', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(code='nomatch', message='Number has to be 10 digit', regex='^.{10}$')])),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('join_date', models.DateField(auto_now_add=True)),
                ('standard', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
                ('roll_no', models.PositiveIntegerField(unique=True)),
                ('ranking', models.PositiveIntegerField(unique=True)),
                ('relatives', models.ManyToManyField(related_name='relative', to='myschool.Relatives')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(default='Test', max_length=20)),
                ('no_of_chapters', models.IntegerField()),
                ('total_duration', models.CharField(max_length=10)),
                ('duration_per_class', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0.5), django.core.validators.MaxValueValidator(2)])),
                ('classroom', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='subject_cls', to='myschool.Classroom')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('join_date', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('salary', models.CharField(max_length=10)),
                ('subject', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_sub', to='myschool.Subject')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='subjects',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stu_sub', to='myschool.Subject'),
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
