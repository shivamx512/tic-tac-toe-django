# Generated by Django 4.2 on 2024-03-11 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_tictactoeboard_game_borad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tictactoeboard',
            name='cell_00',
            field=models.CharField(blank=True, choices=[('', 'Empty'), ('X', 'X'), ('O', 'O')], default='', max_length=1),
        ),
        migrations.AlterField(
            model_name='tictactoeboard',
            name='cell_01',
            field=models.CharField(blank=True, choices=[('', 'Empty'), ('X', 'X'), ('O', 'O')], default='', max_length=1),
        ),
        migrations.AlterField(
            model_name='tictactoeboard',
            name='cell_02',
            field=models.CharField(blank=True, choices=[('', 'Empty'), ('X', 'X'), ('O', 'O')], default='', max_length=1),
        ),
        migrations.AlterField(
            model_name='tictactoeboard',
            name='cell_10',
            field=models.CharField(blank=True, choices=[('', 'Empty'), ('X', 'X'), ('O', 'O')], default='', max_length=1),
        ),
        migrations.AlterField(
            model_name='tictactoeboard',
            name='cell_11',
            field=models.CharField(blank=True, choices=[('', 'Empty'), ('X', 'X'), ('O', 'O')], default='', max_length=1),
        ),
        migrations.AlterField(
            model_name='tictactoeboard',
            name='cell_12',
            field=models.CharField(blank=True, choices=[('', 'Empty'), ('X', 'X'), ('O', 'O')], default='', max_length=1),
        ),
        migrations.AlterField(
            model_name='tictactoeboard',
            name='cell_20',
            field=models.CharField(blank=True, choices=[('', 'Empty'), ('X', 'X'), ('O', 'O')], default='', max_length=1),
        ),
        migrations.AlterField(
            model_name='tictactoeboard',
            name='cell_21',
            field=models.CharField(blank=True, choices=[('', 'Empty'), ('X', 'X'), ('O', 'O')], default='', max_length=1),
        ),
        migrations.AlterField(
            model_name='tictactoeboard',
            name='cell_22',
            field=models.CharField(blank=True, choices=[('', 'Empty'), ('X', 'X'), ('O', 'O')], default='', max_length=1),
        ),
    ]
