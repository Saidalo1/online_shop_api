# Generated by Django 4.1 on 2022-09-03 09:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ComputerSpareParts', '0008_rename_numberofcores_сomputersparepart_сores_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='', max_length=500)),
                ('created_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='CSPImages',
            new_name='Images',
        ),
        migrations.RenameField(
            model_name='basket',
            old_name='computersparepart',
            new_name='computer_spare_part',
        ),
        migrations.RenameField(
            model_name='images',
            old_name='computerSparePart',
            new_name='computer_spare_part',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='computersparepart',
            new_name='computer_spare_part',
        ),
        migrations.RenameField(
            model_name='party',
            old_name='computersparepart',
            new_name='computer_spare_part',
        ),
        migrations.RenameField(
            model_name='payments',
            old_name='computersparepart',
            new_name='computer_spare_part',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='computersparepart',
            new_name='computer_spare_part',
        ),
        migrations.RenameModel(
            old_name='СomputerSparePart',
            new_name='ComputerSparePart',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.AddField(
            model_name='comments',
            name='computer_spare_part',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ComputerSpareParts.computersparepart'),
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]