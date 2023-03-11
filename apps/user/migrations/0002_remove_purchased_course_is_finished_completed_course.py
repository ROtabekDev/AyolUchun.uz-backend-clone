# Generated by Django 4.1.7 on 2023-03-11 03:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchased_course',
            name='is_finished',
        ),
        migrations.CreateModel(
            name='Completed_course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='O`zgartirilgan vaqti')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course', verbose_name='Kurs')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Foydalanuvchi')),
            ],
            options={
                'verbose_name': 'Tugatilgan kurs',
                'verbose_name_plural': 'Tugatilgan kurslar',
            },
        ),
    ]
