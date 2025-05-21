from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import ToolViewSet, ProjectView, ReviewView, ContactRequestCreateView, AboutView, ConsultView

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Моё APi",
        default_version='v1',
        description="Описание",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register(r'tools', ToolViewSet)
router.register(r'projects', ProjectView)
router.register(r'reviews', ReviewView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/contact/', ContactRequestCreateView.as_view()),
    path('api/about/', AboutView.as_view()),
    path('api/consult/', ConsultView.as_view()),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),
]