from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'testimonials', views.TestimonialViewSet, basename='testimonial')
router.register(r'payments', views.PaymentViewSet, basename='payment')
router.register(r'applicants', views.ApplicantsViewSet, basename='applicant')
router.register(r'applications', views.ApplicationsViewSet, basename='application')
router.register(r'schools', views.SchoolsViewSet, basename='school')


urlpatterns = [ 
    path('', include(router.urls)),

    # path("view_application/<int:application_id>/",views.view_application),
    # path("view_payment/<int:payment_id>/",views.view_payment),
    # path("view_school/<int:school_id>/",views.view_school),
    # path("view_applicant/<int:applicant_id>/",views.view_applicant),
    # #edit application
    # path("edit_application/<int:application_id>",views.edit_application),
    # #edit applicant info
    # path("edit_applicant/<int:applicant_id>",views.edit_applicant),
    # #upload testimonial file 
    # #view applications
    # path("applications/",views.view_applications),
    # #view applications for user with counts
    # path('my-applications/<int:applicant_id>/',views.view_personal_applications)

]