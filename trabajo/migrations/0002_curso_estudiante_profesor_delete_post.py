# Generated by Django 4.1.7 on 2023-03-14 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trabajo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('comision', models.IntegerField()),
                ('fecha_inicio', models.DateField(null=True)),
                ('descripcion', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=256)),
                ('apellido', models.CharField(max_length=256)),
                ('dni', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('fecha_nacimiento', models.DateField(null=True)),
                ('comision', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=256)),
                ('apellido', models.CharField(max_length=256)),
                ('dni', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('fecha_nacimiento', models.DateField(null=True)),
                ('profesion', models.CharField(max_length=128, null=True)),
                ('bio', models.TextField(null=True)),
                ('comision', models.CharField(max_length=256, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]