from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from .choices import CATEGORY_CHOICES, LEVEL_CHOICES, WORK_TYPE_CHOICES

class ContactRequest(models.Model):
    phone = PhoneNumberField(verbose_name=_("Телефон"))
    email = models.EmailField(verbose_name=_("Электронная почта"))
    file = models.FileField(upload_to='uploads/', verbose_name=_("Файл"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))

    def __str__(self):
        return f"{self.phone} - {self.email}"

    class Meta:
        verbose_name = _('Контактная заявка')
        verbose_name_plural = _('Контактные заявки')
        ordering = ['id']


class Provide(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Название"))
    description = models.TextField(verbose_name=_("Описание"))
    category = models.CharField(max_length=255, verbose_name=_("Категория"))
    icon = models.CharField(max_length=255, verbose_name=_("Иконка"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Предоставляемая услуга')
        verbose_name_plural = _('Предоставляемые услуги')
        ordering = ['id']


class About(models.Model):
    heading = models.CharField(max_length=255, verbose_name=_("Заголовок"))
    subheading = models.TextField(verbose_name=_("Подзаголовок"))
    founder_name = models.CharField(max_length=100, verbose_name=_("Имя основателя"))
    founder_role = models.CharField(max_length=100, verbose_name=_("Должность основателя"))
    founder_image = models.ImageField(upload_to='founders/', verbose_name=_("Фото основателя"))

    class Meta:
        verbose_name = _('О нас')
        verbose_name_plural = _('О нас')
        ordering = ['id']


class Tool(models.Model):
    name = models.CharField(max_length=20, verbose_name=_("Название"))
    icon = models.ImageField(upload_to="tools/", verbose_name=_("Иконка"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Инструмент')
        verbose_name_plural = _('Инструменты')
        ordering = ['id']


class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Название"))
    photo = models.ImageField(upload_to="tools/", verbose_name=_("Изображение"))
    category = models.CharField(max_length=255, verbose_name=_("Категория"))
    url = models.URLField(blank=True, null=True, verbose_name=_("Ссылка"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Проект')
        verbose_name_plural = _('Проекты')
        ordering = ['id']


class Review(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Имя"))
    position = models.CharField(max_length=255, verbose_name=_("Должность"))
    message = models.TextField(verbose_name=_("Сообщение"))
    photo = models.ImageField(upload_to='review/', blank=True, null=True, verbose_name=_("Фото"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Отзыв')
        verbose_name_plural = _('Отзывы')
        ordering = ['id']


class Consult(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Имя"))
    phone = PhoneNumberField(verbose_name=_("Телефон"))
    text = models.TextField(verbose_name=_("Сообщение"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Консультация')
        verbose_name_plural = _('Консультации')
        ordering = ['id']


class Dizain(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Название"))
    text = models.TextField(verbose_name=_("Описание"))
    image = models.ImageField(upload_to='dizain/', verbose_name=_("Изображение"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Дизайн')
        verbose_name_plural = _('Дизайны')
        ordering = ['id']


class Image(models.Model):
    image = models.ImageField(upload_to='images/', verbose_name=_("Изображение"))

    class Meta:
        verbose_name = _('Изображение')
        verbose_name_plural = _('Изображения')
        ordering = ['id']


class Job(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Название"))
    description = models.TextField(verbose_name=_("Описание"))
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, verbose_name=_("Категория"))
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES, verbose_name=_("Уровень"))
    work_type = models.CharField(max_length=20, choices=WORK_TYPE_CHOICES, verbose_name=_("Тип работы"))
    is_active = models.BooleanField(default=True, verbose_name=_("Активна"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Вакансия')
        verbose_name_plural = _('Вакансии')
        ordering = ['id']


class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications', verbose_name=_("Вакансия"))
    name = models.CharField(max_length=100, verbose_name=_("Имя"))
    phone = PhoneNumberField(verbose_name=_("Телефон"))
    email = models.EmailField(verbose_name=_("Электронная почта"))
    linkedin_url = models.URLField(blank=True, verbose_name=_("Ссылка на LinkedIn"))
    file = models.FileField(upload_to='resumes/', verbose_name=_("Резюме"))
    applied_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата подачи"))

    def __str__(self):
        return f"{self.name} -> {self.job.title}"

    class Meta:
        verbose_name = _('Заявка на вакансию')
        verbose_name_plural = _('Заявки на вакансии')
        ordering = ['id']


class Meropriyatie(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Название"))
    description = models.TextField(verbose_name=_("Описание"))
    date = models.DateTimeField(verbose_name=_("Дата и время"))
    location = models.CharField(max_length=255, verbose_name=_("Место проведения"))
    image = models.ImageField(upload_to='meropriyatie/', verbose_name=_("Изображение"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Мероприятие')
        verbose_name_plural = _('Мероприятия')
        ordering = ['id']
