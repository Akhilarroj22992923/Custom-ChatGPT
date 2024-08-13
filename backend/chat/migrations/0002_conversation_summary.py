from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        #adds a new field to an existing model.
        migrations.AddField(
            model_name='conversation',
            name='summary',
            field=models.TextField(blank=True, null=True),
        ),
    ]