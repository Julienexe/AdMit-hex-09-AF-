from django.urls import path
from . import views

urlpatterns = [ 
    path("",views.home),
    path("schools/",views.schools),
    path("create_school/",views.create_school),
]