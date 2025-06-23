from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import StudentViewSet  # Use absolute import

router = DefaultRouter()
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]