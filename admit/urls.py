from django.urls import path
from . import views

urlpatterns = [ 
    path("",views.home),
    path("schools/",views.schools),
    path("create_school/",views.create_school),
    path("submit_application/",views.submit_application),
    path("submit_payment/",views.submit_payment),
    path("view_application/<int:application_id>/",views.view_application),
    path("view_payment/<int:payment_id>/",views.view_payment),
    path("view_school/<int:school_id>/",views.view_school),
    path("view_applicant/<int:applicant_id>/",views.view_applicant),
    path("view_applications/",views.view_applications),
    #edit application
    path("edit_application/<int:application_id>",views.edit_application),
    #edit applicant info
    path("edit_applicant/<int:applicant_id>",views.edit_applicant),

]