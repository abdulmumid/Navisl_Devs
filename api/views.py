from rest_framework import generics, viewsets, mixins

from .models import (
    ContactRequest, Services, About, Tool, Project, Review, Consult,
    Dizain, Image, Job, JobApplication, Meropriyatie
)
from .serializers import (
    ContactRequestSerializer, ServicesSerializer, AboutSerializer, ToolSerializer, ProjectSerializer,
    ReviewSerializer, ConsultSerializer, DizainSerializer, ImageSerializer,
    JobSerializer, JobApplicationSerializer, MeropriyatieSerializer
)

# --- Создание новой заявки через API (POST) ---
class ContactRequestCreateView(generics.CreateAPIView):
    queryset = ContactRequest.objects.all()
    serializer_class = ContactRequestSerializer


# --- Только GET и POST для услуг ---
class ServicesViewSet(viewsets.GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


# --- Получение первого объекта "О нас" (GET) ---
class AboutView(generics.RetrieveAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

    def get_object(self):
        return About.objects.first()


# --- Только GET и POST для инструментов ---
class ToolViewSet(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer


# --- Проекты: GET список и детали ---
class ProjectView(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


# --- Отзывы: GET список и детали ---
class ReviewView(viewsets.GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.RetrieveModelMixin):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


# --- POST только для консультаций ---
class ConsultView(viewsets.GenericViewSet,
                  mixins.CreateModelMixin):
    queryset = Consult.objects.all()
    serializer_class = ConsultSerializer


# --- Дизайны: только GET и POST ---
class DizainViewSet(viewsets.GenericViewSet,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin):
    queryset = Dizain.objects.all()
    serializer_class = DizainSerializer


# --- Изображения: только GET и POST ---
class ImageViewSet(viewsets.GenericViewSet,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


# --- Вакансии: только GET ---
class JobViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Job.objects.filter(is_active=True).order_by('-created_at')
    serializer_class = JobSerializer


# --- Заявки на вакансии: GET и POST ---
class JobApplicationViewSet(viewsets.GenericViewSet,
                            mixins.CreateModelMixin,
                            mixins.ListModelMixin,
                            mixins.RetrieveModelMixin):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer


# --- Мероприятия: GET и POST ---
class MeropriyatieViewSet(viewsets.GenericViewSet,
                          mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.CreateModelMixin):
    queryset = Meropriyatie.objects.all()
    serializer_class = MeropriyatieSerializer
