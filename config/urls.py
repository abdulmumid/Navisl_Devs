from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="NavisDevs APi",
        default_version='v1',
        description="""
🔹 **NavisDevs** — IT-компания, специализирующаяся на разработке сайтов и мобильных приложений для бизнеса.

Этот API обеспечивает доступ к данным сайта NavisDevs и предоставляет следующие возможности:

### 📦 Основные модули:
- 📲 **ContactRequest** — заявки на консультацию
- 🛠 **Tools** — список технологий, которые мы используем в разработке
- 🧩 **Services** — услуги, которые предлагает компания
- 📁 **Projects** — наши реализованные проекты
- 💬 **Reviews** — отзывы клиентов
- 👥 **Jobs** — открытые вакансии в компании
- 📄 **Job Applications** — отклики на вакансии
- 🎨 **Dizain** — примеры дизайна
- 📸 **Image** — изображения для различных разделов сайта
- 📅 **Meropriyatie** — предстоящие мероприятия

### 🧰 Технологии:
- Django, Django REST Framework
- PostgreSQL
- Swagger (drf-yasg)

Все эндпоинты доступны через этот интерфейс Swagger, и их можно тестировать прямо здесь.
        """,
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),
    path('', include('api.urls')),
]