# Generated by Django 4.1.7 on 2023-03-10 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='O`zgartirilgan vaqti')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Pul miqdori')),
                ('payment_type', models.CharField(choices=[('Payme', 'Payme'), ('Click', 'Click'), ('Apelsin', 'Apelsin'), ('KPay', 'KPay'), ('Visa', 'Visa'), ('MasterCard', 'MasterCard')], max_length=15, verbose_name='To`lov turi')),
                ('payment_status', models.CharField(choices=[('Succes', 'Muvaffaqiyatli'), ('Error', 'Xato'), ('In_progress', 'Jarayonda')], max_length=15, verbose_name='To`lov holati')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]