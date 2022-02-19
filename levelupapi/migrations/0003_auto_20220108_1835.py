# Generated by Django 3.2.9 on 2022-01-08 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0002_auto_20211222_0309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='event',
            name='event_date',
        ),
        migrations.RemoveField(
            model_name='event',
            name='game_title',
        ),
        migrations.RemoveField(
            model_name='event',
            name='location',
        ),
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AddField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='levelupapi.gamer'),
        ),
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='game',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='levelupapi.game'),
        ),
    ]
