# Generated by Django 5.2 on 2025-06-05 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0003_alter_poster_date_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink',
            name='category',
            field=models.CharField(choices=[('hot', 'Горячее'), ('cold', 'Холодное'), ('seasonal', 'Сезонное'), ('not', 'Неопределенно')], default='not', max_length=100),
        ),
    ]
