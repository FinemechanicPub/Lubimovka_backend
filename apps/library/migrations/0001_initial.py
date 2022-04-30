# Generated by Django 3.2.11 on 2022-01-29 14:40

import apps.library.utilities
import apps.library.validators
import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('afisha', '0001_initial'),
        ('articles', '0001_initial'),
        ('core', '0001_initial'),
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('tag', models.CharField(help_text='Не более 40 символов', max_length=40, verbose_name='Достижения в виде тега')),
            ],
            options={
                'verbose_name': 'Достижение',
                'verbose_name_plural': 'Достижения',
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('quote', models.CharField(max_length=200, verbose_name='Цитата')),
                ('biography', models.TextField(max_length=3000, verbose_name='Текст про автора')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
                'ordering': ('person__last_name',),
            },
        ),
        migrations.CreateModel(
            name='MasterClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.TextField(max_length=500, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Мастер-класс',
                'verbose_name_plural': 'Мастер-классы',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OtherLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('link', models.URLField(max_length=500, verbose_name='Ссылка')),
                ('is_pinned', models.BooleanField(help_text='Закрепить ссылку вверху страницы?', verbose_name='Закрепить ссылку')),
                ('order_number', models.PositiveSmallIntegerField(help_text='Указывается для формирования порядка вывода информации', verbose_name='Порядковый номер')),
            ],
            options={
                'verbose_name': 'Публикации и другие материалы',
                'verbose_name_plural': 'Публикации и другие материалы',
                'ordering': ('order_number',),
            },
        ),
        migrations.CreateModel(
            name='OtherPlay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=70, verbose_name='Название')),
                ('link', models.URLField(max_length=1000, verbose_name='Ссылка на скачивание файла')),
            ],
            options={
                'verbose_name': 'Другая пьеса',
                'verbose_name_plural': 'Другие пьесы',
            },
        ),
        migrations.CreateModel(
            name='ParticipationApplicationFestival',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('birth_year', models.PositiveSmallIntegerField(validators=[apps.library.validators.year_validator], verbose_name='Год рождения')),
                ('city', models.CharField(max_length=50, verbose_name='Город проживания')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(help_text='Номер телефона указывается в формате +7', max_length=128, region=None, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=100, verbose_name='Электронная почта')),
                ('title', models.CharField(max_length=200, verbose_name='Название пьесы')),
                ('year', models.PositiveSmallIntegerField(validators=[apps.library.validators.year_validator], verbose_name='Год написания')),
                ('file', models.FileField(help_text="Файл в одно из форматов ('doc', 'docx', 'txt', 'odt', 'pdf')", upload_to=apps.feedback.utilities.generate_upload_path, validators=[django.core.validators.FileExtensionValidator(('doc', 'docx', 'txt', 'odt', 'pdf'))], verbose_name='Файл')),
                ('verified', models.BooleanField(choices=[(True, 'Да'), (False, 'Нет')], default=False, verbose_name='Проверена?')),
            ],
            options={
                'verbose_name': 'Заявление на участие',
                'verbose_name_plural': 'Заявления на участие',
            },
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, verbose_name='Название спектакля')),
                ('main_image', models.ImageField(upload_to='performances/', verbose_name='Главное изображение')),
                ('bottom_image', models.ImageField(upload_to='performances/', verbose_name='Изображение внизу страницы')),
                ('video', models.URLField(blank=True, null=True, unique=True, verbose_name='Видео')),
                ('description', models.TextField(max_length=500, verbose_name='Краткое описание')),
                ('text', models.TextField(max_length=500, verbose_name='Полное описание')),
                ('age_limit', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(18)], verbose_name='Возрастное ограничение')),
                ('duration', models.DurationField(default=datetime.timedelta(seconds=5100), verbose_name='Продолжительность')),
                ('events', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='performance', to='afisha.commonevent', verbose_name='События')),
                ('images_in_block', models.ManyToManyField(blank=True, to='core.Image', verbose_name='Фотографии спектакля в блоке фотографий')),
            ],
            options={
                'verbose_name': 'Спектакль',
                'verbose_name_plural': 'Спектакли',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Play',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=70, unique=True, verbose_name='Название пьесы')),
                ('city', models.CharField(max_length=200, verbose_name='Город')),
                ('year', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1990), django.core.validators.MaxValueValidator(2200)], verbose_name='Год написания пьесы')),
                ('url_download', models.URLField(blank=True, null=True, unique=True, verbose_name='Ссылка на скачивание пьесы')),
                ('url_reading', models.URLField(blank=True, null=True, unique=True, verbose_name='Ссылка на читку')),
                ('is_draft', models.BooleanField(default=True, verbose_name='Черновик')),
                ('festival', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='plays', to='info.festival', verbose_name='Фестиваль')),
            ],
            options={
                'verbose_name': 'Пьеса',
                'verbose_name_plural': 'Пьесы',
            },
        ),
        migrations.CreateModel(
            name='ProgramType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Название программы')),
                ('slug', models.SlugField(max_length=40, unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Программа',
                'verbose_name_plural': 'Программы',
            },
        ),
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.TextField(max_length=500, verbose_name='Описание')),
                ('events', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='reading', to='afisha.commonevent', verbose_name='События')),
            ],
            options={
                'verbose_name': 'Читка',
                'verbose_name_plural': 'Читки',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('masterclass', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_members', to='library.masterclass', verbose_name='Мастер-класс')),
                ('performance', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_members', to='library.performance', verbose_name='Спектакль')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='team_members', to='core.person', verbose_name='Член команды')),
                ('reading', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_members', to='library.reading', verbose_name='Читка')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='team_members', to='core.role', verbose_name='Роль')),
            ],
            options={
                'verbose_name': 'Член команды',
                'verbose_name_plural': 'Члены команды',
                'ordering': ('role',),
            },
        ),
        migrations.CreateModel(
            name='SocialNetworkLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(choices=[('fb', 'Facebook'), ('inst', 'Instagram'), ('ytube', 'YouTube'), ('tlgrm', 'Telegram'), ('vk', 'Вконтакте')], max_length=200, verbose_name='Название')),
                ('link', models.URLField(max_length=500, verbose_name='Ссылка')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_networks', to='library.author', verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Ссылка на социальную сеть',
                'verbose_name_plural': 'Ссылки на социальные сети',
            },
        ),
        migrations.AddField(
            model_name='reading',
            name='persons',
            field=models.ManyToManyField(related_name='readings', through='library.TeamMember', to='core.Person', verbose_name='Члены команды'),
        ),
        migrations.AddField(
            model_name='reading',
            name='play',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='readings', to='library.play', verbose_name='Пьеса'),
        ),
        migrations.AddField(
            model_name='reading',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='readings', to='articles.project', verbose_name='Проект'),
        ),
        migrations.AddField(
            model_name='play',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='plays', to='library.programtype', verbose_name='Программа'),
        ),
        migrations.CreateModel(
            name='PerformanceReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('reviewer_name', models.CharField(max_length=100, verbose_name='Имя зрителя')),
                ('text', models.TextField(max_length=500, verbose_name='Текст отзыва')),
                ('url', models.URLField(blank=True, null=True, unique=True, verbose_name='Ссылка на отзыв')),
                ('pub_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')),
                ('performance', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reviews', to='library.performance', verbose_name='Спектакль')),
            ],
            options={
                'verbose_name': 'Отзыв зрителя на спектакль',
                'verbose_name_plural': 'Отзывы зрителей на спектакль',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='PerformanceMediaReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('media_name', models.CharField(max_length=100, verbose_name='Название медиа ресурса')),
                ('text', models.TextField(max_length=500, verbose_name='Текст отзыва')),
                ('image', models.ImageField(upload_to='reviews/', verbose_name='Изображение')),
                ('url', models.URLField(blank=True, null=True, unique=True, verbose_name='Ссылка на отзыв')),
                ('pub_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')),
                ('performance', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='media_reviews', to='library.performance', verbose_name='Спектакль')),
            ],
            options={
                'verbose_name': 'Медиа отзыв на спектакль',
                'verbose_name_plural': 'Медиа отзывы на спектакль',
                'ordering': ('-created',),
            },
        ),
        migrations.AddField(
            model_name='performance',
            name='persons',
            field=models.ManyToManyField(related_name='performances', through='library.TeamMember', to='core.Person', verbose_name='Члены команды'),
        ),
        migrations.AddField(
            model_name='performance',
            name='play',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='performances', to='library.play', verbose_name='Пьеса'),
        ),
        migrations.AddField(
            model_name='performance',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='performances', to='articles.project', verbose_name='Проект'),
        ),
        migrations.AddConstraint(
            model_name='participationapplicationfestival',
            constraint=models.UniqueConstraint(fields=('first_name', 'last_name', 'birth_year', 'city', 'phone_number', 'email', 'title', 'year'), name='unique_application'),
        ),
        migrations.AddField(
            model_name='otherplay',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='other_plays', to='library.author', verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='otherlink',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='other_links', to='library.author', verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='masterclass',
            name='events',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='masterclass', to='afisha.commonevent', verbose_name='События'),
        ),
        migrations.AddField(
            model_name='masterclass',
            name='persons',
            field=models.ManyToManyField(related_name='masterclasses', through='library.TeamMember', to='core.Person', verbose_name='Члены команды'),
        ),
        migrations.AddField(
            model_name='masterclass',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='masterclasses', to='articles.project', verbose_name='Проект'),
        ),
        migrations.AddField(
            model_name='author',
            name='achievements',
            field=models.ManyToManyField(blank=True, related_name='authors', to='library.Achievement', verbose_name='Достижения'),
        ),
        migrations.AddField(
            model_name='author',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='core.person', verbose_name='Человек'),
        ),
        migrations.AddField(
            model_name='author',
            name='plays',
            field=models.ManyToManyField(blank=True, related_name='authors', to='library.Play', verbose_name='Пьесы автора'),
        ),
        migrations.AddConstraint(
            model_name='teammember',
            constraint=models.UniqueConstraint(fields=('person', 'role', 'performance'), name='unique_person_role_per_performance'),
        ),
        migrations.AddConstraint(
            model_name='teammember',
            constraint=models.UniqueConstraint(fields=('person', 'role', 'reading'), name='unique_person_role_per_reading'),
        ),
        migrations.AddConstraint(
            model_name='teammember',
            constraint=models.UniqueConstraint(fields=('person', 'role', 'masterclass'), name='unique_person_role_per_masterclass'),
        ),
        migrations.AddConstraint(
            model_name='socialnetworklink',
            constraint=models.UniqueConstraint(fields=('author', 'name'), name='unique_social_network'),
        ),
        migrations.AddConstraint(
            model_name='play',
            constraint=models.UniqueConstraint(fields=('name', 'festival'), name='unique_play'),
        ),
        migrations.AddConstraint(
            model_name='otherplay',
            constraint=models.UniqueConstraint(fields=('author', 'name'), name='unique_other_play'),
        ),
        migrations.AddConstraint(
            model_name='otherlink',
            constraint=models.UniqueConstraint(fields=('author', 'name'), name='unique_link'),
        ),
        migrations.AlterField(
            model_name='play',
            name='year',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(2200)], verbose_name='Год написания пьесы'),
        ),
        migrations.AlterField(
            model_name='play',
            name='url_download',
            field=models.FileField(default=1, max_length=200, upload_to='plays', verbose_name='Текст пьесы'),
            preserve_default=False,
        ),
        migrations.AlterModelOptions(
            name='participationapplicationfestival',
            options={'verbose_name': 'Заявка на участие', 'verbose_name_plural': 'Заявки на участие'},
        ),
    ]
