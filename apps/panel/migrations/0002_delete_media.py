from django.db import migrations

def delete_media_table(apps, schema_editor):
    # Assuming the media table is named 'panel_media'
    schema_editor.execute("DROP TABLE IF EXISTS panel_media;")

class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(delete_media_table, atomic=False),  # Set atomic=False to run outside a transaction
    ]