# Generated by Django 4.2.6 on 2023-12-26 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourismapp', '0007_book_userid_travel_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
