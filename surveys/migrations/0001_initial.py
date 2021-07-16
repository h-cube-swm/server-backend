# Generated by Django 3.2.5 on 2021-07-14 19:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='설문 제목을 넣어주세요')),
                ('description', models.TextField(default='설문 설명을 넣어주세요', null=True)),
                ('status', models.CharField(choices=[('editing', 'Editing'), ('published', 'Published'), ('closed', 'Closed'), ('deleted', 'Deleted')], default='editing', max_length=20)),
                ('contents', models.JSONField(default=dict)),
                ('link', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('view', models.TextField(default='설문 view타입을 넣어주세요')),
            ],
            options={
                'db_table': 'surveys',
            },
        ),
    ]
