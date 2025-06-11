from rest_framework import serializers
from .models import (
    ContactRequest, About, Tool, Project, Review, Consult,
    Dizain, Image, Job, JobApplication, Meropriyatie
)


class ContactRequestSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(label="Телефон")
    email = serializers.EmailField(label="Электронная почта")
    file = serializers.FileField(label="Файл")
    created_at = serializers.DateTimeField(label="Дата создания", read_only=True)

    class Meta:
        model = ContactRequest
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    heading = serializers.CharField(label="Заголовок")
    subheading = serializers.CharField(label="Подзаголовок")
    founder_name = serializers.CharField(label="Имя основателя")
    founder_role = serializers.CharField(label="Должность основателя")
    founder_image = serializers.ImageField(label="Фото основателя")

    class Meta:
        model = About
        fields = '__all__'


class ToolSerializer(serializers.ModelSerializer):
    name = serializers.CharField(label="Название")
    icon = serializers.ImageField(label="Иконка")

    class Meta:
        model = Tool
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    title = serializers.CharField(label="Название проекта")
    photo = serializers.ImageField(label="Фото проекта")
    category = serializers.CharField(label="Категория")
    url = serializers.URLField(label="Ссылка на проект", required=False)

    class Meta:
        model = Project
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    name = serializers.CharField(label="Имя")
    position = serializers.CharField(label="Должность")
    message = serializers.CharField(label="Сообщение")
    photo = serializers.ImageField(label="Фото", required=False)
    created_at = serializers.DateTimeField(label="Дата", read_only=True)

    class Meta:
        model = Review
        fields = '__all__'


class ConsultSerializer(serializers.ModelSerializer):
    name = serializers.CharField(label="Имя")
    phone = serializers.CharField(label="Телефон")
    text = serializers.CharField(label="Сообщение")
    created_at = serializers.DateTimeField(label="Дата", read_only=True)

    class Meta:
        model = Consult
        fields = '__all__'


class DizainSerializer(serializers.ModelSerializer):
    title = serializers.CharField(label="Название")
    text = serializers.CharField(label="Описание")
    image = serializers.ImageField(label="Изображение")

    class Meta:
        model = Dizain
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(label="Изображение")

    class Meta:
        model = Image
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    title = serializers.CharField(label="Название")
    description = serializers.CharField(label="Описание")
    category = serializers.CharField(label="Категория")
    level = serializers.CharField(label="Уровень")
    work_type = serializers.CharField(label="Тип работы")
    is_active = serializers.BooleanField(label="Активна")
    created_at = serializers.DateTimeField(label="Дата создания", read_only=True)

    class Meta:
        model = Job
        fields = '__all__'


class JobApplicationSerializer(serializers.ModelSerializer):
    job = serializers.PrimaryKeyRelatedField(label="Вакансия", queryset=Job.objects.all())
    name = serializers.CharField(label="Имя")
    phone = serializers.CharField(label="Телефон")
    email = serializers.EmailField(label="Email")
    linkedin_url = serializers.URLField(label="LinkedIn", required=False)
    file = serializers.FileField(label="Файл")
    applied_at = serializers.DateTimeField(label="Дата подачи", read_only=True)

    class Meta:
        model = JobApplication
        fields = '__all__'


class MeropriyatieSerializer(serializers.ModelSerializer):
    title = serializers.CharField(label="Название")
    description = serializers.CharField(label="Описание")
    date = serializers.DateTimeField(label="Дата")
    location = serializers.CharField(label="Место проведения")
    image = serializers.ImageField(label="Изображение")

    class Meta:
        model = Meropriyatie
        fields = '__all__'
