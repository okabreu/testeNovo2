# Generated by Django 4.2.5 on 2024-05-29 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_autor_autorfk_itemlivro_qtd_livro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprestimo',
            name='data_devolucao',
        ),
        migrations.RemoveField(
            model_name='emprestimo',
            name='livro',
        ),
        migrations.RemoveField(
            model_name='emprestimo',
            name='valor_total_emprestimo',
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='data_emprestimo',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]