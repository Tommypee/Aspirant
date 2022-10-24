# Generated by Django 4.1.1 on 2022-10-24 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ssce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_type', models.PositiveSmallIntegerField(choices=[('Eng', 'English'), ('Math', 'Mathematics'), ('che', 'Chemistry'), ('Phy', 'Physics'), ('Bio', 'Biology'), ('civic', 'Civic Education'), ('Gov', 'Government'), ('eco', 'Economics'), ('com', 'Commerce'), ('acc', 'Financial Accounting'), ('Liter', 'Literature_in_English'), ('Agric', 'Agricultural Science')])),
                ('grade_type', models.PositiveSmallIntegerField(choices=[('A1', 'A1'), ('B2', 'B2'), ('B3', 'B3'), ('C4', 'C4'), ('C5', 'C5'), ('C6', 'C6'), ('D7', 'D7'), ('E8', 'E8'), ('E8', 'E8'), ('F9', 'F9')])),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]