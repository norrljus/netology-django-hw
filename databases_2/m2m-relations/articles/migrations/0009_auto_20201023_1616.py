# Generated by Django 3.1.2 on 2020-10-23 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20201022_1923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scope',
            name='is_main',
        ),
        migrations.AddField(
            model_name='articlescope',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='Основной'),
        ),
        migrations.AlterField(
            model_name='scope',
            name='article_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='art_name', to='articles.article'),
        ),
        migrations.AlterField(
            model_name='scope',
            name='scope_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scp_name', to='articles.articlescope'),
        ),
    ]