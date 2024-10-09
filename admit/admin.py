from django.contrib import admin
from .models import School, Applicant, Application, Payment

admin.site.register(School)
admin.site.register(Applicant)
admin.site.register(Application)
admin.site.register(Payment)

