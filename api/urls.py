from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ContactRequestCreateView,
    AboutView,
    ToolViewSet,
    ProjectView,
    ReviewView,
    ConsultView,
    DizainViewSet,
    ImageViewSet,
    JobViewSet,
    JobApplicationViewSet,
    MeropriyatieViewSet,
)

router = DefaultRouter()
router.register('consult', ConsultView, basename='consult')
router.register('tools', ToolViewSet, basename='tools')
router.register('projects', ProjectView, basename='projects') 
router.register('reviews', ReviewView, basename='reviews')
router.register('dizains', DizainViewSet, basename='dizains')
router.register('images', ImageViewSet, basename='images')
router.register('jobs', JobViewSet, basename='jobs')
router.register('job-applications', JobApplicationViewSet, basename='jobapplications')
router.register('meropriyaties', MeropriyatieViewSet, basename='meropriyaties')

urlpatterns = [
    path('api/contact/', ContactRequestCreateView.as_view(), name='contact-request'),
    path('api/about/', AboutView.as_view(), name='about'),
    path('api/', include(router.urls)),
]
