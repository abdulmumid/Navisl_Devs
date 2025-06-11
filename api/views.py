from rest_framework import generics, mixins, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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


# --- Просмотр списка услуг (GET) и создание услуги (POST) ---
class ProvideListCreateView(APIView):
    def get(self, request):
        queryset = Provide.objects.filter(is_active=True).order_by('-created_at')
        serializer = ProvideSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProvideSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# --- Получение информации "О нас" (только GET первого объекта) ---
class AboutView(generics.RetrieveAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

    def get_object(self):
        return About.objects.first()


# --- Инструменты: только GET и POST ---
class ToolListCreateView(APIView):
    def get(self, request):
        tools = Tool.objects.all()
        serializer = ToolSerializer(tools, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ToolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# --- Проекты ---
class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetailView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


# --- Отзывы ---
class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetailView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


# --- Консультация ---
class ConsultCreateView(generics.CreateAPIView):
    queryset = Consult.objects.all()
    serializer_class = ConsultSerializer


# --- Дизайн ---
class DizainListCreateView(APIView):
    def get(self, request):
        queryset = Dizain.objects.all()
        serializer = DizainSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DizainSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# --- Изображения ---
class ImageListCreateView(APIView):
    def get(self, request):
        queryset = Image.objects.all()
        serializer = ImageSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# --- Вакансии (только GET активных) ---
class JobListView(generics.ListAPIView):
    queryset = Job.objects.filter(is_active=True).order_by('-created_at')
    serializer_class = JobSerializer

class JobDetailView(generics.RetrieveAPIView):
    queryset = Job.objects.filter(is_active=True)
    serializer_class = JobSerializer


# --- Отклики на вакансии ---
class JobApplicationListCreateView(APIView):
    def get(self, request):
        queryset = JobApplication.objects.all()
        serializer = JobApplicationSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JobApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# --- Мероприятия ---
class MeropriyatieListCreateView(APIView):
    def get(self, request):
        queryset = Meropriyatie.objects.all()
        serializer = MeropriyatieSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MeropriyatieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
