# Generated by Django 2.2.3 on 2019-08-05 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_remove_board_writer'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='writer',
            field=models.CharField(default=True, max_length=200),
        ),
    ]
