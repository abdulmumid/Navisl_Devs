from rest_framework import serializers
from .models import (
    About,
    ContactRequest,
    Provide,
    Consult,
    Dizain,
    Image,
    Job,
    JobApplication,
    Meropriyatie,
    Project,
    Review,
    Tool,
)


# Сериализатор для обработки заявок на контакт.
class ContactRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactRequest
        fields = ['id', 'phone', 'email', 'created_at']
        read_only_fields = ['id', 'created_at']  # Эти поля нельзя изменять, только для чтения

# Сериализатор для предоставляемой услуги с дополнительным методом получения списка характеристик
class ProvideSerializer(serializers.ModelSerializer):
    features = serializers.SerializerMethodField()

    class Meta:
        model = Provide
        fields = '__all__'

    # Возвращает список характеристик предоставляемой услуги (метод модели)
    def get_features(self, obj):
        return obj.get_features_list()

# Сериализатор для страницы "О компании"
class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'

# Сериализатор для инструментов/тулов
class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = '__all__'

# Сериализатор для проектов компании
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

# Сериализатор для отзывов с методом получения характеристик
class ReviewSerializer(serializers.ModelSerializer):
    features = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = '__all__'

    # Получает список характеристик отзыва (метод модели)
    def get_features(self, obj):
        return obj.get_features_list()
    
# Сериализатор для запросов на консультацию
class ConsultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consult
        fields = '__all__'

# Сериализатор для дизайна
class DizainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dizain
        fields = '__all__'
        
# Сериализатор для изображений
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

# Сериализатор для вакансий
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

# Сериализатор для откликов на вакансии
class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = '__all__'

    def validate_file(self, file):
        allowed_types = {'application/pdf', 'image/svg+xml', 'image/png'}
        allowed_extensions = {'pdf', 'svg', 'png'}

        if file:
            # Проверяем MIME-тип
            if file.content_type not in allowed_types:
                raise serializers.ValidationError(
                    f'Файл "{file.name}" имеет недопустимый формат! Разрешены только PDF, SVG, PNG.'
                )

            # Проверяем расширение файла
            ext = os.path.splitext(file.name)[1][1:].lower()
            if ext not in allowed_extensions:
                raise serializers.ValidationError(
                    f'Файл "{file.name}" имеет недопустимое расширение! Разрешены только .pdf, .svg, .png.'
                )  # ← Закрыл кавычки

        return file

# Сериализатор для мероприятий компании
class MeropriyatieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meropriyatie
        fields = '__all__'
