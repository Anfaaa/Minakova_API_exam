from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from task1.views import TaskViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Task API",
      default_version='v1',
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

