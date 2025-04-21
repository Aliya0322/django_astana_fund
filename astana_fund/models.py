from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.utils import timezone
from django.core.validators import FileExtensionValidator


class Event(models.Model):
    STATUS_CHOICES = [
        ('current', 'Предстоящее'),
        ('past', 'Прошедшее'),
    ]

    title = models.CharField(
        max_length=255,
        verbose_name='Название мероприятия'
    )
    description = models.TextField(
        verbose_name='Описание мероприятия'
    )
    short_description = models.CharField(
        max_length=500,
        verbose_name='Краткое описание'
    )
    program = models.TextField(
        verbose_name='Программа мероприятия',
        blank=True,
        null=True,
        help_text='Детальное описание программы мероприятия. Можно использовать HTML-разметку'
    )
    start_date = models.DateTimeField(
        verbose_name='Дата и время начала'
    )
    end_date = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Дата и время окончания'
    )
    location = models.CharField(
        max_length=255,
        verbose_name='Место проведения'
    )
    address = models.CharField(
        max_length=500,
        verbose_name='Адрес'
    )
    image = models.ImageField(
        upload_to='events/',
        verbose_name='Изображение',
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        verbose_name='Статус мероприятия'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активно'
    )

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
        ordering = ['-start_date']
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['start_date', 'end_date']),
            models.Index(fields=['is_active']),
        ]

    def __str__(self):
        return self.title

    @property
    def is_current(self):
        """Проверяет, является ли мероприятие текущим (предстоящим)"""
        return self.status == 'current'

    @property
    def is_past(self):
        """Проверяет, является ли мероприятие прошедшим"""
        return self.status == 'past'

class MediaPublication(models.Model):
    PUBLICATION_TYPE_CHOICES = [
        ('article', 'Статья'),
        ('interview', 'Интервью'),
        ('report', 'Репортаж'),
        ('photo', 'Фоторепортаж'),
        ('video', 'Видеоматериал'),
    ]

    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок публикации'
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        verbose_name='URL-адрес',
        blank=True
    )
    publication_date = models.DateField(
        verbose_name='Дата публикации',
        default=timezone.now
    )
    author = models.CharField(
        max_length=255,
        verbose_name='Автор',
        blank=True
    )
    source = models.CharField(
        max_length=255,
        verbose_name='Источник (СМИ)'
    )
    source_url = models.URLField(
        verbose_name='Ссылка на оригинал',
        blank=True
    )
    short_description = models.TextField(
        verbose_name='Краткое описание',
        max_length=500
    )
    full_content = models.TextField(
        verbose_name='Полный текст',
        blank=True
    )
    publication_type = models.CharField(
        max_length=20,
        choices=PUBLICATION_TYPE_CHOICES,
        verbose_name='Тип публикации',
        default='article'
    )
    main_image = models.ImageField(
        upload_to='media_publications/',
        verbose_name='Главное изображение',
        blank=True,
        null=True
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )

    class Meta:
        verbose_name = 'Публикация СМИ'
        verbose_name_plural = 'Публикации СМИ'
        ordering = ['-publication_date']
        indexes = [
            models.Index(fields=['publication_type']),
            models.Index(fields=['is_published']),
            models.Index(fields=['publication_date']),
        ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('media_detail', kwargs={'slug': self.slug})

    @property
    def formatted_date(self):
        """Возвращает дату в формате 'd E Y' (например, '21 ноября 2024')"""
        months = {
            1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля',
            5: 'мая', 6: 'июня', 7: 'июля', 8: 'августа',
            9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'
        }
        return f"{self.publication_date.day} {months[self.publication_date.month]} {self.publication_date.year}"


class Project(models.Model):
    STATUS_CHOICES = [
        ('current', 'Текущий проект'),
        ('completed', 'Завершен'),
        ('permanent', 'Постоянный'),
    ]

    title = models.CharField(
        max_length=255,
        verbose_name='Название проекта'
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        verbose_name='URL-адрес',
        blank=True
    )
    short_description = models.CharField(
        max_length=500,
        verbose_name='Краткое описание'
    )
    full_description = models.TextField(
        verbose_name='Полное описание',
        blank=True
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        verbose_name='Статус проекта',
        default='current'
    )
    start_date = models.DateField(
        verbose_name='Дата начала',
        null=True,
        blank=True
    )
    end_date = models.DateField(
        verbose_name='Дата окончания',
        null=True,
        blank=True
    )
    location = models.CharField(
        max_length=255,
        verbose_name='Место реализации'
    )
    main_image = models.ImageField(
        upload_to='projects/',
        verbose_name='Главное изображение',
        null=True,
        blank=True
    )
    is_featured = models.BooleanField(
        default=False,
        verbose_name='Рекомендуемый проект'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['-is_featured', '-start_date']
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['is_featured']),
        ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'slug': self.slug})

    @property
    def duration(self):
        """Форматированное отображение периода реализации"""
        if self.status == 'permanent':
            return f"С {self.start_date.year} года"
        elif self.status == 'completed' and self.start_date and self.end_date:
            return f"{self.start_date.year}-{self.end_date.year}"
        elif self.start_date:
            return f"С {self.start_date.year}"
        return ""

    @property
    def status_label(self):
        """Возвращает метку статуса для отображения"""
        return dict(self.STATUS_CHOICES).get(self.status, '')


class InterestingBase(models.Model):
    """Абстрактная базовая модель для всех типов материалов"""
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField(verbose_name='Описание')
    thumbnail = models.ImageField(
        upload_to='interesting/thumbs/',
        verbose_name='Обложка',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    views = models.PositiveIntegerField(default=0, verbose_name='Просмотры')

    class Meta:
        abstract = True
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('interesting_detail', kwargs={'slug': self.slug, 'type': self.type})


class Video(InterestingBase):
    """Модель для видео материалов"""
    video_file = models.FileField(
        upload_to='interesting/videos/',
        verbose_name='Видео файл',
        validators=[FileExtensionValidator(allowed_extensions=['mp4', 'mov', 'avi'])],
        null=True,
        blank=True
    )
    duration = models.DurationField(verbose_name='Длительность', null=True, blank=True)


    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

    @property
    def type(self):
        return 'video'


class Music(InterestingBase):
    """Модель для музыкальных материалов"""
    audio_file = models.FileField(
        upload_to='interesting/music/',
        verbose_name='Аудио файл',
        validators=[FileExtensionValidator(allowed_extensions=['mp3', 'wav'])],
        null=True,
        blank=True
    )
    duration = models.DurationField(verbose_name='Длительность', null=True, blank=True)
    artist = models.CharField(max_length=255, verbose_name='Исполнитель', blank=True)

    class Meta:
        verbose_name = 'Музыка'
        verbose_name_plural = 'Музыка'

    @property
    def type(self):
        return 'music'


class Article(InterestingBase):
    """Модель для статей"""
    content = models.TextField(verbose_name='Содержание статьи')
    author = models.CharField(max_length=255, verbose_name='Автор')
    reading_time = models.PositiveIntegerField(
        verbose_name='Время чтения (мин)',
        default=5
    )
    tags = models.ManyToManyField(
        'InterestingTag',
        related_name='articles',
        verbose_name='Теги',
        blank=True
    )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    @property
    def type(self):
        return 'article'


class InterestingTag(models.Model):
    """Модель для тегов материалов"""
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

