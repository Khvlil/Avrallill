from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("loader", views.loader, name="loader"),
    path("contact_us", views.contact_us, name="contact_us"),
    path('get_work_type/<str:type_>/',
         views.get_project_types, name='get_work_type'),
    path('get_version/<str:version>/', views.get_version, name='get_version'),
    path("studyCase/<str:project_name>",
         views.show_project, name="show_project"),
]
