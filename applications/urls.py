from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'testimonials', views.TestimonialViewSet, basename='testimonial')
router.register(r'applicants', views.ApplicantsViewSet, basename='applicant')
router.register(r'applications', views.ApplicationsViewSet, basename='application')