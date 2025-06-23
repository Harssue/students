from django.urls import path
from .views import AddStudent, DeleteStudent, EditStudent

urlpatterns = [
    path('add-student/', AddStudent.as_view(), name='add-student'),
    path('delete-student/', DeleteStudent.as_view(), name='delete-student'),
    path('edit-student/<int:id>/', EditStudent.as_view(), name='edit-student'),
]