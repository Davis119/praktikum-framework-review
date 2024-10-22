from django.urls import path
from . import views
from django.urls import include, path
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from .views import StudentsViewSet

urlpatterns = [
   path('about', views.about, name="about"),
   path('', views.homepage),
   path('student', views.student_index, name='student_index'), # Read
   path('student/create/', views.student_create, name='student_create'),# Create
   path('student/update/<int:student_id>/', views.student_update, name='student_update'),
   path('student/delete/<int:student_id>', views.student_delete, name='student_delete'),
   path('api/', include(router.urls)), # Ini akan menambahkan semua URL yang dibutuhkan untuk API
]

