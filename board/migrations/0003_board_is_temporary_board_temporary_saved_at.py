# Generated by Django 4.1.4 on 2023-05-25 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("board", "0002_alter_board_board_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="board",
            name="is_temporary",
            field=models.BooleanField(default=False, verbose_name="임시저장 여부"),
        ),
        migrations.AddField(
            model_name="board",
            name="temporary_saved_at",
            field=models.DateTimeField(blank=True, null=True, verbose_name="임시저장 시간"),
        ),
    ]