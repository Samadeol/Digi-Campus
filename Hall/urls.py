from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.apiOverview, name="api_security"),
    path('student-list/',views.studentlist, name="student-list"),
    path('student-detail/<str:pk>',views.studentdetail, name="student-detail"),
    path('student-create/',views.studentcreate, name="student-create"),
    path('student-delete/<str:pk>',views.studentdelete, name="student-delete"),
]