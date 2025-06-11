from rest_framework import generics, viewsets, mixins

from .models import (
    ContactRequest, Provide, About, Tool, Project, Review, Consult,
    Dizain, Image, Job, JobApplication, Meropriyatie
)
from .serializers import (
    ContactRequestSerializer, ProvideSerializer, AboutSerializer, ToolSerializer, ProjectSerializer,
    ReviewSerializer, ConsultSerializer, DizainSerializer, ImageSerializer,
    JobSerializer, JobApplicationSerializer, MeropriyatieSerializer
)


# --- Создание новой заявки через API ---
class ContactRequestCreateView(generics.CreateAPIView):
    queryset = ContactRequest.objects.all()
    serializer_class = ContactRequestSerializer

# --- Просмотр и редактирование информации о предоставляемых услугах ---
class ProvideViewSet(viewsets.ModelViewSet):
    queryset = Provide.objects.all()
    serializer_class = ProvideSerializer

    def get_queryset(self):
        # Возвращаем только активные услуги
        return self.queryset.filter(is_active=True).order_by('-created_at')

# --- Получение информации "О нас" (первый объект) ---
class AboutView(generics.RetrieveAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

    def get_object(self):
        # Возвращаем первый объект About (предполагается один объект)
        return About.objects.first()


# --- CRUD для инструментов ---
class ToolViewSet(viewsets.ModelViewSet):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer


# --- Просмотр проектов (список и детали) ---
class ProjectView(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


# --- Просмотр отзывов (список и детали) ---
class ReviewView(viewsets.GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.RetrieveModelMixin):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


# --- Создание заявки на консультацию ---
class ConsultView(viewsets.GenericViewSet,
                  mixins.CreateModelMixin):
    queryset = Consult.objects.all()
    serializer_class = ConsultSerializer


# --- CRUD для дизайнов ---
class DizainViewSet(viewsets.ModelViewSet):
    queryset = Dizain.objects.all()
    serializer_class = DizainSerializer


# --- CRUD для изображений ---
class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


# --- Только чтение вакансий (активные) ---
class JobViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Job.objects.filter(is_active=True).order_by('-created_at')
    serializer_class = JobSerializer


# --- Работа с откликами на вакансии: создание, просмотр списка, просмотр деталей ---
class JobApplicationViewSet(viewsets.GenericViewSet,
                            mixins.CreateModelMixin,
                            mixins.ListModelMixin,
                            mixins.RetrieveModelMixin):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer


# --- CRUD для мероприятий ---
class MeropriyatieViewSet(viewsets.ModelViewSet):
    queryset = Meropriyatie.objects.all()
    serializer_class = MeropriyatieSerializer
