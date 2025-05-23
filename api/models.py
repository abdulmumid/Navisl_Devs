from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = _('Сервис')
        verbose_name_plural = _('Сервисы')
        ordering = ['id']

class ContactRequest(models.Model):
    phone = PhoneNumberField()
    email = models.EmailField()
    file = models.FileField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.phone} - {self.email}"
    class Meta:
        verbose_name = _('Контактная заявка')
        verbose_name_plural = _('Контактные заявки')
        ordering = ['id']
    

class Panel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = _('Панель')
        verbose_name_plural = _('Панели')
        ordering = ['id']

class About(models.Model):
    heading = models.CharField(max_length=255)  
    subheading = models.TextField()            
    founder_name = models.CharField(max_length=100)  
    founder_role = models.CharField(max_length=100)  
    founder_image = models.ImageField(upload_to='founders/') 

    class Meta:
        verbose_name = _('О нас')
        verbose_name_plural = _('О нас')
        ordering = ['id']

class Tool(models.Model):
    name = models.CharField(max_length=20)
    icon = models.ImageField(upload_to="tools/")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = _('Инструмент')
        verbose_name_plural = _('Инструменты')
        ordering = ['id']

class Project(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="tools/")
    category = models.CharField(max_length=255)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = _('Проект')
        verbose_name_plural = _('Проекты')
        ordering = ['id']
    
class Review(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    message = models.TextField(max_length=255)
    photo = models.ImageField(upload_to='review/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = _('Отзыв')
        verbose_name_plural = _('Отзывы')
        ordering = ['id']
    
class Consult(models.Model):
    name = models.CharField(max_length=255)
    phone = PhoneNumberField()
    text = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = _('Консультация')
        verbose_name_plural = _('Консультации')
        ordering = ['id']
    
class Dizain(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(upload_to='dizain/')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = _('Дизайн')
        verbose_name_plural = _('Дизайны')
        ordering = ['id']
    
class Image(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name = _('Изображение')
        verbose_name_plural = _('Изображения')
        ordering = ['id']


class Job(models.Model):
    LEVEL_CHOICES = [
        ('Intern', 'Intern'),
        ('Junior', 'Junior'),
        ('Middle', 'Middle'),
        ('Senior', 'Senior'),
    ]
    WORK_TYPE_CHOICES = [
        ('Remote', 'Удалённо'),
        ('Office', 'Офис'),
        ('Hybrid', 'Гибридный график'),
        ('Full-time', 'Полный рабочий день'),
    ]
    CATEGORY_CHOICES = [
        ('Frontend', 'Frontend'),
        ('Backend', 'Backend'),
        ('Design', 'Дизайн'),
        ('Management', 'Менеджмент'),
        ('SMM', 'SMM'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES)
    work_type = models.CharField(max_length=20, choices=WORK_TYPE_CHOICES)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = _('Вакансия')
        verbose_name_plural = _('Вакансии')
        ordering = ['id']


class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    name = models.CharField(max_length=100)
    phone = PhoneNumberField()
    email = models.EmailField()
    linkedin_url = models.URLField(blank=True)
    file = models.FileField(upload_to='resumes/')
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} -> {self.job.title}"
    class Meta:
        verbose_name = _('Заявка на вакансию')
        verbose_name_plural = _('Заявки на вакансии')
        ordering = ['id']
    

class Meropriyatie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='meropriyatie/')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = _('Мероприятие')
        verbose_name_plural = _('Мероприятия')
        ordering = ['id']
