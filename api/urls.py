from django.urls import path, include
from .views import (
    ContactRequestCreateView,
    AboutView,
    ToolViewSet,
    ProjectView,
    ReviewView,
    ConsultView,
    DizainViewSet,
    ServiceViewSet,
    ImageViewSet,
    JobViewSet,
    JobApplicationViewSet,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('tools', ToolViewSet)
router.register('project', ProjectView)
router.register('review', ReviewView)
router.register('dizain', DizainViewSet)
router.register('services', ServiceViewSet)
router.register('images', ImageViewSet)
router.register('job', JobViewSet)
router.register('job-application', JobApplicationViewSet)

urlpatterns = [
    path('api/contact/', ContactRequestCreateView.as_view(), name='contact-request'),
    path('api/consult/', ConsultView.as_view(), name='consult-request'),
    path('about/', AboutView.as_view()),
    path('api/', include(router.urls)),
]

