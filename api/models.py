from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from .choices import CATEGORY_CHOICES, LEVEL_CHOICES, WORK_TYPE_CHOICES

# Модель для хранения заявок на консультацию через форму обратной связи
class ContactRequest(models.Model):
    phone = PhoneNumberField()  # Номер телефона пользователя
    email = models.EmailField()  # Электронная почта пользователя
    file = models.FileField(upload_to='uploads/')  # Загруженный файл (например, резюме или ТЗ)
    created_at = models.DateTimeField(auto_now_add=True)  # Дата и время создания заявки

    def __str__(self):
        return f"{self.phone} - {self.email}"

    class Meta:
        verbose_name = _('Контактная заявка')
        verbose_name_plural = _('Контактные заявки')
        ordering = ['id']


# Модель для представления услуг или панелей на сайте
class Services(models.Model):
    title = models.CharField(max_length=255)  # Название услуги
    description = models.TextField()  # Описание услуги
    category = models.CharField(max_length=255)  # Категория услуги
    icon = models.CharField(max_length=255)  # Иконка (CSS-класс или имя файла)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Панель')
        verbose_name_plural = _('Панели')
        ordering = ['id']


# Модель "О нас"
class About(models.Model):
    heading = models.CharField(max_length=255)  # Заголовок секции
    subheading = models.TextField()  # Подзаголовок или описание
    founder_name = models.CharField(max_length=100)  # Имя основателя
    founder_role = models.CharField(max_length=100)  # Должность основателя
    founder_image = models.ImageField(upload_to='founders/')  # Фото основателя

    class Meta:
        verbose_name = _('О нас')
        verbose_name_plural = _('О нас')
        ordering = ['id']


# Модель для хранения используемых технологий и инструментов
class Tool(models.Model):
    name = models.CharField(max_length=20)  # Название инструмента
    icon = models.ImageField(upload_to="tools/")  # Иконка/изображение инструмента

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Инструмент')
        verbose_name_plural = _('Инструменты')
        ordering = ['id']


# Модель для портфолио/проектов
class Project(models.Model):
    title = models.CharField(max_length=100)  # Название проекта
    photo = models.ImageField(upload_to="tools/")  # Изображение проекта
    category = models.CharField(max_length=255)  # Категория проекта
    url = models.URLField(blank=True, null=True)  # Ссылка на проект

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Проект')
        verbose_name_plural = _('Проекты')
        ordering = ['id']


# Модель для отзывов клиентов
class Review(models.Model):
    name = models.CharField(max_length=255)  # Имя клиента
    position = models.CharField(max_length=255)  # Должность клиента
    message = models.TextField()  # Сообщение/отзыв
    photo = models.ImageField(upload_to='review/', blank=True, null=True)  # Фото клиента
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания отзыва

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Отзыв')
        verbose_name_plural = _('Отзывы')
        ordering = ['id']


# Модель для заявки на консультацию
class Consult(models.Model):
    name = models.CharField(max_length=255)  # Имя пользователя
    phone = PhoneNumberField()  # Телефон
    text = models.TextField()  # Сообщение
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Консультация')
        verbose_name_plural = _('Консультации')
        ordering = ['id']


# Модель для секции "Дизайн"
class Dizain(models.Model):
    title = models.CharField(max_length=255)  # Название работы
    text = models.TextField()  # Описание
    image = models.ImageField(upload_to='dizain/')  # Изображение

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Дизайн')
        verbose_name_plural = _('Дизайны')
        ordering = ['id']


# Модель для изображений на сайте
class Image(models.Model):
    title = models.CharField(max_length=255)  # Название изображения
    image = models.ImageField(upload_to='images/')  # Сам файл изображения

    class Meta:
        verbose_name = _('Изображение')
        verbose_name_plural = _('Изображения')
        ordering = ['id']


# Модель для вакансий
class Job(models.Model):
    
    title = models.CharField(max_length=255)  # Название вакансии
    description = models.TextField()  # Описание вакансии
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)  # Категория
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES)  # Уровень
    work_type = models.CharField(max_length=20, choices=WORK_TYPE_CHOICES)  # Тип работы
    is_active = models.BooleanField(default=True)  # Активна ли вакансия
    created_at = models.DateTimeField(auto_now_add=True)  # Дата публикации

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Вакансия')
        verbose_name_plural = _('Вакансии')
        ordering = ['id']


# Модель заявок на вакансии
class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')  # Вакансия
    name = models.CharField(max_length=100)  # Имя кандидата
    phone = PhoneNumberField()  # Телефон
    email = models.EmailField()  # Email
    linkedin_url = models.URLField(blank=True)  # Ссылка на LinkedIn
    file = models.FileField(upload_to='resumes/')  # Файл резюме
    applied_at = models.DateTimeField(auto_now_add=True)  # Дата подачи заявки

    def __str__(self):
        return f"{self.name} -> {self.job.title}"

    class Meta:
        verbose_name = _('Заявка на вакансию')
        verbose_name_plural = _('Заявки на вакансии')
        ordering = ['id']


# Модель для мероприятий
class Meropriyatie(models.Model):
    title = models.CharField(max_length=255)  # Название мероприятия
    description = models.TextField()  # Описание мероприятия
    date = models.DateTimeField()  # Дата и время проведения
    location = models.CharField(max_length=255)  # Место проведения
    image = models.ImageField(upload_to='meropriyatie/')  # Изображение мероприятия

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Мероприятие')
        verbose_name_plural = _('Мероприятия')
        ordering = ['id']
