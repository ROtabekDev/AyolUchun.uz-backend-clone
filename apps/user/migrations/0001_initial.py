# Generated by Django 4.1.7 on 2023-03-12 06:11

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='O`zgartirilgan vaqti')),
                ('first_name', models.CharField(max_length=100, verbose_name='Ism')),
                ('last_name', models.CharField(max_length=100, verbose_name='Familiya')),
                ('patronymic', models.CharField(blank=True, max_length=100, null=True, verbose_name='Otasining ismi')),
                ('phone_number', models.CharField(error_messages={'unique': 'Bu telefon nomer ro`yhatdan o`tgan!'}, max_length=15, unique=True, validators=[django.core.validators.RegexValidator(message='Iltimos telefon nomerni to`g`ri kiriting', regex='^[+][998]{3}?[0-9]{9}$')], verbose_name='Telefon nomer')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='Elektron pochta')),
                ('email_is_approad', models.BooleanField(default=False, verbose_name='Elektron pochta holati')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Foydalanuvchi',
                'verbose_name_plural': 'Barcha foydalanuvchilar',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='O`zgartirilgan vaqti')),
                ('name', models.CharField(max_length=150, verbose_name='Nomi')),
                ('slug', models.SlugField(max_length=150, verbose_name='Slugi')),
            ],
            options={
                'verbose_name': 'Mamlakat',
                'verbose_name_plural': 'Mamlakatlar',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='O`zgartirilgan vaqti')),
                ('name', models.CharField(max_length=150, verbose_name='Nomi')),
                ('slug', models.SlugField(max_length=150, verbose_name='Slugi')),
                ('country_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.country')),
            ],
            options={
                'verbose_name': 'Viloyat',
                'verbose_name_plural': 'Viloyatlar',
            },
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='O`zgartirilgan vaqti')),
                ('title', models.CharField(max_length=150, verbose_name='Nomi')),
                ('slug', models.SlugField(max_length=150, verbose_name='Slugi')),
            ],
            options={
                'verbose_name': 'Mutaxassislik',
                'verbose_name_plural': 'Mutaxassisliklar',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='O`zgartirilgan vaqti')),
                ('profile_pic', models.ImageField(default='user/user_profile/profile_pic/default-user-image.png', upload_to='user/user_profile/profile_pic/', verbose_name='Rasm')),
                ('birthday', models.DateTimeField(blank=True, null=True, verbose_name='Tug`ilgan sanasi')),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Erkak'), ('Female', 'Ayol')], max_length=10, null=True, verbose_name='Jinsi')),
                ('zip_code', models.PositiveIntegerField(blank=True, null=True, verbose_name='Pochta indeksi')),
                ('address', models.CharField(blank=True, max_length=250, null=True, verbose_name='Manzil')),
                ('facebook_profile', models.CharField(blank=True, max_length=150, null=True, verbose_name='Facebook sahifa')),
                ('instagram_profile', models.CharField(blank=True, max_length=150, null=True, verbose_name='Instagram sahifa')),
                ('imkon_profile', models.CharField(blank=True, max_length=150, null=True, verbose_name='Imkon sahifa')),
                ('linkedin_profile', models.CharField(blank=True, max_length=150, null=True, verbose_name='Linkedin sahifa')),
                ('telegram_profile', models.CharField(blank=True, max_length=150, null=True, verbose_name='Telegram sahifa')),
                ('workplace', models.CharField(blank=True, max_length=250, null=True, verbose_name='Ish joyi')),
                ('position', models.CharField(blank=True, max_length=150, null=True, verbose_name='Lavozimi')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Foydalanuvchi haqida ma`lumot')),
                ('country_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.country')),
                ('region_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.region')),
                ('specialty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.speciality')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Foydalanuvchi')),
            ],
            options={
                'verbose_name': 'Profil',
                'verbose_name_plural': 'Profillar',
            },
        ),
    ]
