# Generated by Django 4.0.2 on 2022-03-02 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_employee_salary_alter_student_roll'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='roll',
            field=models.IntegerField(),
        ),
    ]