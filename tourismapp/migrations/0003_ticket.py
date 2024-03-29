# Generated by Django 4.2.7 on 2023-12-21 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourismapp', '0002_alter_travel_t_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('num_people', models.IntegerField()),
            ],
        ),
    ]
