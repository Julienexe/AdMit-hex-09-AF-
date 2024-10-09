from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser

from .models import School, Applicant, Application, Payment
from .serializers import SchoolSerializer, ApplicantSerializer, ApplicationSerializer, PaymentSerializer,TestimonialSerializer

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

#create applicant
@api_view(['POST'])
def create_applicant(request):
    serialized_applicant = ApplicantSerializer(data=request.data)
    if serialized_applicant.is_valid():
        serialized_applicant.save()
        return Response(serialized_applicant.data)
    return Response(serialized_applicant.errors)

#create a view for the applicants to submit their applications
@api_view(['POST'])
def submit_application(request):
    serialized_application = ApplicationSerializer(data=request.data)
    if serialized_application.is_valid():
        serialized_application.save()
        return Response(serialized_application.data)
    return Response(serialized_application.errors)

#create a view for the applicants to submit their payments
@api_view(['POST'])
def submit_payment(request):
    serialized_payment = PaymentSerializer(data=request.data)
    if serialized_payment.is_valid():
        serialized_payment.save()
        return Response(serialized_payment.data)
    return Response(serialized_payment.errors)

#view for someone to view a specific application
@api_view(['GET'])
def view_application(request,application_id):
    application = Application.objects.get(id=application_id)
    serialized_application = ApplicationSerializer(application)
    return Response(serialized_application.data)

#view for someone to view a specific payment
@api_view(['GET'])
def view_payment(request,payment_id):
    payment = Payment.objects.get(id=payment_id)
    serialized_payment = PaymentSerializer(payment)
    return Response(serialized_payment.data)

#view for someone to view a specific school
@api_view(['GET'])
def view_school(request,school_id):
    school = School.objects.get(id=school_id)
    serialized_school = SchoolSerializer(school)
    return Response(serialized_school.data)

#view for someone to view a specific applicant
@api_view(['GET'])
def view_applicant(request,applicant_id):
    applicant = Applicant.objects.get(id=applicant_id)
    serialized_applicant = ApplicantSerializer(applicant)
    return Response(serialized_applicant.data)

#view to edit a specific application
@api_view(['PUT'])
def edit_application(request,application_id):
    application = Application.objects.get(id=application_id)
    serialized_application = ApplicationSerializer(instance=application, data=request.data)
    if serialized_application.is_valid():
        serialized_application.save()
        return Response(serialized_application.data)
    return Response(serialized_application.errors)

#view to edit applicant information
@api_view(['PUT'])
def edit_applicant(request,applicant_id):
    applicant = Applicant.objects.get(id=applicant_id)
    serialized_applicant = ApplicantSerializer(instance=applicant, data=request.data)
    if serialized_applicant.is_valid():
        serialized_applicant.save()
        return Response(serialized_applicant.data)
    return Response(serialized_applicant.errors)

#viewset to handle testimonial uploads
class TestimonialViewSet(ModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = TestimonialSerializer

    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        #applicant = Applicant.objects.get(id=self.request.user.id)
        serializer.save(
                       file=self.request.data.get('file'))
        return Response({"message":"Testimonial uploaded successfully"})