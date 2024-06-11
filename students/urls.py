from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student/<int:student_id>/', views.student_profile, name='student_profile'),
    path('student/<int:student_id>/edit/', views.edit_student_profile, name='edit_student_profile'),
]
