from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    HomeView as Home,
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

# Создаем роутер DRF для автоматической генерации URL для viewset-ов
router = DefaultRouter()

# Регистрируем viewset-ы в роутере с префиксами и базовыми именами
router.register('consult', ConsultView, basename='consult')
router.register('tools', ToolViewSet, basename='tools')
router.register('projects', ProjectView, basename='projects') 
router.register('reviews', ReviewView, basename='reviews')
router.register('dizains', DizainViewSet, basename='dizains')
router.register('images', ImageViewSet, basename='images')
router.register('jobs', JobViewSet, basename='jobs')
router.register('job-applications', JobApplicationViewSet, basename='jobapplications')
router.register('meropriyaties', MeropriyatieViewSet, basename='meropriyaties')

# Определяем urlpatterns для ручных и автоматических маршрутов
urlpatterns = [
    path('', Home, name='home'),  # Главная страница
    # Отдельный путь для создания заявки контакта
    path('api/contact/', ContactRequestCreateView.as_view(), name='contact-request'),
    # Отдельный путь для получения информации 'About' (единственный объект)
    path('api/about/', AboutView.as_view(), name='about'),
    # Включаем все маршруты из роутера (для viewset-ов)
    path('api/', include(router.urls)),
]

