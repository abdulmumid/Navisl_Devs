from rest_framework import generics, viewsets
from .models import Service, ContactRequest, About, Tool, Project, Review, Consult, Dizain, Image, Job, JobApplication, Meropriyatie
from .serializers import ServiceSerializer, ContactRequestSerializer, AboutSerializer, ToolSerializer, ProjectSerializer, ReviewSerializer, ConsultSerializer, DizainSerializer, ImageSerializer, JobSerializer, JobApplicationSerializer, MeropriyatieSerializer



class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer



class ContactRequestCreateView(generics.CreateAPIView):
    queryset = ContactRequest.objects.all()
    serializer_class = ContactRequestSerializer


class AboutView(generics.RetrieveAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

    def get_object(self):
        return About.objects.first()

class ToolViewSet(viewsets.ModelViewSet):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer

class ProjectView(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ReviewView(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ConsultView(generics.CreateAPIView):
    queryset = Consult.objects.all()
    serializer_class = ConsultSerializer

class DizainViewSet(viewsets.ModelViewSet):
    queryset = Dizain.objects.all()
    serializer_class = DizainSerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class JobViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Job.objects.filter(is_active=True).order_by('-created_at')
    serializer_class = JobSerializer


class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer

class MeropriyatieViewSet(viewsets.ModelViewSet):
    queryset = Meropriyatie.objects.all()
    serializer_class = MeropriyatieSerializer
