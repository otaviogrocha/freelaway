# Generated by Django 4.0.4 on 2022-05-05 21:32

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_alter_jobs_arquivo_final_alter_jobs_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='categoria',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('D', 'Design'), ('EV', 'Edição de Vídeo')], max_length=4),
        ),
    ]
