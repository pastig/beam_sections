from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('generate_report/', views.generate_report, name='generate_report'),
    path('report_template/', views.report_template, name='report_template'),  # Add this line
]
