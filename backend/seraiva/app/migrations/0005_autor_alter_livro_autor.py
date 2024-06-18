# Generated by Django 4.2.5 on 2024-05-26 22:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_livro_autor_delete_autor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biografia', models.CharField(max_length=2000)),
                ('foto', models.CharField(max_length=1000)),
                ('autorFk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='livro',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.autor'),
        ),
    ]
