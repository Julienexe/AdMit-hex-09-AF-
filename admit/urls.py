from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'payments', views.PaymentViewSet, basename='payment')
router.register(r'schools', views.SchoolsViewSet, basename='school')


urlpatterns = [ 
    path('', include(router.urls)),

]