from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import School, Applicant, Application, Payment
from .serializers import SchoolSerializer, ApplicantSerializer, ApplicationSerializer, PaymentSerializer

@api_view(['GET'])
def home(request):
    return Response({"message":"Welcome to the admit API"})

@api_view(['GET'])
def schools(request):
    schools = School.objects.all()
    serialized_schools = SchoolSerializer(schools, many=True)
    return Response(serialized_schools.data)

@api_view(['POST'])
def create_school(request):
    serialized_school = SchoolSerializer(data=request.data)
    if serialized_school.is_valid():
        serialized_school.save()
        return Response(serialized_school.data)
    return Response(serialized_school.errors)

#create a view for the applicants to submit their applications
@api_view(['POST'])
def submit_application(request):
    serialized_application = ApplicationSerializer(data=request.data)
    if serialized_application.is_valid():
        serialized_application.save()
        return Response(serialized_application.data)
    return Response(serialized_application.errors)
