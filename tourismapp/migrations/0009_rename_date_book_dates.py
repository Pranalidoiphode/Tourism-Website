# Generated by Django 4.2.6 on 2023-12-27 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourismapp', '0008_book_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='date',
            new_name='dates',
        ),
    ]
