# Generated by Django 4.2.7 on 2023-12-21 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourismapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='t_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]