# Generated by Django 4.0.1 on 2022-02-05 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idea', '0002_alter_idea_related'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='related',
            field=models.CharField(choices=[('Social', 'Social'), ('Educational', 'Educational'), ('IT', 'IT'), ('Law', 'Law'), ('Personal', 'Personal'), ('Metal', 'Mental'), ('Environmental', 'Environmental'), ('Economical', 'Economical'), ('Health', 'Health'), ('Other', 'Other')], default='Other', max_length=100),
        ),
    ]
