# Generated by Django 3.2.13 on 2022-07-04 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("canned_views", "0008_rename_cannedviews_cannedview_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="historicalcannedview",
            options={
                "get_latest_by": ("history_date", "history_id"),
                "ordering": ("-history_date", "-history_id"),
                "verbose_name": "historical Canned View",
                "verbose_name_plural": "historical Canned Views",
            },
        ),
        migrations.AlterField(
            model_name="historicalcannedview",
            name="history_date",
            field=models.DateTimeField(db_index=True),
        ),
    ]
