from django.urls import path
from config import settings
from django.conf.urls.static import static
from .views import (
    ContactRequestCreateView,
    ProvideListCreateView,
    AboutView,
    ToolListCreateView,
    ProjectListView,
    ProjectDetailView,
    ReviewListView,
    ReviewDetailView,
    ConsultCreateView,
    DizainListCreateView,
    ImageListCreateView,
    JobListView,
    JobDetailView,
    JobApplicationListCreateView,
    MeropriyatieListCreateView,
)

urlpatterns = [
    path('api/contact/', ContactRequestCreateView.as_view(), name='contact-request'),
    path('api/about/', AboutView.as_view(), name='about'),

    path('api/provides/', ProvideListCreateView.as_view(), name='provides'),
    path('api/tools/', ToolListCreateView.as_view(), name='tools'),
    path('api/dizains/', DizainListCreateView.as_view(), name='dizains'),
    path('api/images/', ImageListCreateView.as_view(), name='images'),

    path('api/projects/', ProjectListView.as_view(), name='project-list'),
    path('api/projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),

    path('api/reviews/', ReviewListView.as_view(), name='review-list'),
    path('api/reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),

    path('api/consult/', ConsultCreateView.as_view(), name='consult'),

    path('api/jobs/', JobListView.as_view(), name='job-list'),
    path('api/jobs/<int:pk>/', JobDetailView.as_view(), name='job-detail'),

    path('api/job-applications/', JobApplicationListCreateView.as_view(), name='job-applications'),

    path('api/meropriyaties/', MeropriyatieListCreateView.as_view(), name='meropriyaties'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)