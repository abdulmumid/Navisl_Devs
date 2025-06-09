from rest_framework import generics, viewsets, mixins

from .models import (
    ContactRequest, About, Tool, Project, Review, Consult,
    Dizain, Image, Job, JobApplication, Meropriyatie
)
from .serializers import (
    ContactRequestSerializer, AboutSerializer, ToolSerializer, ProjectSerializer,
    ReviewSerializer, ConsultSerializer, DizainSerializer, ImageSerializer,
    JobSerializer, JobApplicationSerializer, MeropriyatieSerializer
)


# --- Создание новой заявки через API ---
class ContactRequestCreateView(generics.CreateAPIView):
    queryset = ContactRequest.objects.all()
    serializer_class = ContactRequestSerializer


# --- Получение информации "О нас" (первый объект) ---
class AboutView(generics.RetrieveAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

    def get_object(self):
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


# --- Только GET и POST для изображений ---
class ImageViewSet(viewsets.GenericViewSet,
                   mixins.ListModelMixin,     # GET /images/
                   mixins.RetrieveModelMixin, # GET /images/<id>/
                   mixins.CreateModelMixin):  # POST /images/
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


# --- Только чтение вакансий (активные) ---
class JobViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Job.objects.filter(is_active=True).order_by('-created_at')
    serializer_class = JobSerializer


# --- Работа с откликами на вакансии ---
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
