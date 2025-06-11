from rest_framework import serializers
from .models import (
    ContactRequest, Services, About, Tool, Project, Review, Consult,
    Dizain, Image, Job, JobApplication, Meropriyatie
)

class ContactRequestSerializer(serializers.ModelSerializer):
    телефон = serializers.CharField(source='phone')
    почта = serializers.EmailField(source='email')
    файл = serializers.FileField(source='file')
    создано = serializers.DateTimeField(source='created_at')

    class Meta:
        model = ContactRequest
        fields = ('id', 'телефон', 'почта', 'файл', 'создано')


class ServicesSerializer(serializers.ModelSerializer):
    название = serializers.CharField(source='title')
    описание = serializers.CharField(source='description')
    категория = serializers.CharField(source='category')
    иконка = serializers.CharField(source='icon')

    class Meta:
        model = Services
        fields = ('id', 'название', 'описание', 'категория', 'иконка')


class AboutSerializer(serializers.ModelSerializer):
    заголовок = serializers.CharField(source='heading')
    подзаголовок = serializers.CharField(source='subheading')
    имя_основателя = serializers.CharField(source='founder_name')
    должность_основателя = serializers.CharField(source='founder_role')
    фото_основателя = serializers.ImageField(source='founder_image')

    class Meta:
        model = About
        fields = ('id', 'заголовок', 'подзаголовок', 'имя_основателя', 'должность_основателя', 'фото_основателя')


class ToolSerializer(serializers.ModelSerializer):
    название = serializers.CharField(source='name')
    иконка = serializers.ImageField(source='icon')

    class Meta:
        model = Tool
        fields = ('id', 'название', 'иконка')


class ProjectSerializer(serializers.ModelSerializer):
    название = serializers.CharField(source='title')
    изображение = serializers.ImageField(source='photo')
    категория = serializers.CharField(source='category')
    ссылка = serializers.URLField(source='url')

    class Meta:
        model = Project
        fields = ('id', 'название', 'изображение', 'категория', 'ссылка')


class ReviewSerializer(serializers.ModelSerializer):
    имя = serializers.CharField(source='name')
    должность = serializers.CharField(source='position')
    сообщение = serializers.CharField(source='message')
    фото = serializers.ImageField(source='photo')
    дата = serializers.DateTimeField(source='created_at')

    class Meta:
        model = Review
        fields = ('id', 'имя', 'должность', 'сообщение', 'фото', 'дата')


class ConsultSerializer(serializers.ModelSerializer):
    имя = serializers.CharField(source='name')
    телефон = serializers.CharField(source='phone')
    сообщение = serializers.CharField(source='text')
    создано = serializers.DateTimeField(source='created_at')

    class Meta:
        model = Consult
        fields = ('id', 'имя', 'телефон', 'сообщение', 'создано')


class DizainSerializer(serializers.ModelSerializer):
    название = serializers.CharField(source='title')
    описание = serializers.CharField(source='text')
    изображение = serializers.ImageField(source='image')

    class Meta:
        model = Dizain
        fields = ('id', 'название', 'описание', 'изображение')


class ImageSerializer(serializers.ModelSerializer):
    изображение = serializers.ImageField(source='image')

    class Meta:
        model = Image
        fields = ('id', 'изображение')


class JobSerializer(serializers.ModelSerializer):
    название = serializers.CharField(source='title')
    описание = serializers.CharField(source='description')
    категория = serializers.CharField(source='category')
    уровень = serializers.CharField(source='level')
    тип_работы = serializers.CharField(source='work_type')
    активна = serializers.BooleanField(source='is_active')
    создано = serializers.DateTimeField(source='created_at')

    class Meta:
        model = Job
        fields = ('id', 'название', 'описание', 'категория', 'уровень', 'тип_работы', 'активна', 'создано')


class JobApplicationSerializer(serializers.ModelSerializer):
    вакансия = serializers.PrimaryKeyRelatedField(source='job', read_only=True)
    имя = serializers.CharField(source='name')
    телефон = serializers.CharField(source='phone')
    почта = serializers.EmailField(source='email')
    linkedin = serializers.URLField(source='linkedin_url')
    файл = serializers.FileField(source='file')
    подано = serializers.DateTimeField(source='applied_at')

    class Meta:
        model = JobApplication
        fields = ('id', 'вакансия', 'имя', 'телефон', 'почта', 'linkedin', 'файл', 'подано')


class MeropriyatieSerializer(serializers.ModelSerializer):
    название = serializers.CharField(source='title')
    описание = serializers.CharField(source='description')
    дата = serializers.DateTimeField(source='date')
    место = serializers.CharField(source='location')
    изображение = serializers.ImageField(source='image')

    class Meta:
        model = Meropriyatie
        fields = ('id', 'название', 'описание', 'дата', 'место', 'изображение')
