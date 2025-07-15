from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.auth.models import User

from .models import School, Applicant, Application, Payment
from .serializers import SchoolSerializer, ApplicantSerializer, ApplicationSerializer, PaymentSerializer,TestimonialSerializer, UserSerializer


class SchoolsViewSet(ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    def perform_create(self, serializer):
        serializer.save()
        return Response({"message": "School created successfully"})

class ApplicantsViewSet(ModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer

    def perform_create(self, serializer):
        serializer.save()
        return Response({"message": "Applicant created successfully"})

class ApplicationsViewSet(ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def perform_create(self, serializer):
        serializer.save()
        return Response({"message": "Application submitted successfully"})
    
    #custom action to view applications made by the logged-in user
    @action(detail=False, methods=['get'], url_path='my-applications')
    def my_applications(self, request):
        user = request.user
        applicant = Applicant.objects.get(user=user)
        applications = Application.objects.filter(applicant=applicant)
        serialized_applications = ApplicationSerializer(applications, many=True)
        return Response(serialized_applications.data)
    
    @action(detail=False, methods=['get'], url_path='pending-applications')
    def pending_applications(self):
        applications = Application.objects.filter(status=Application.Status.PENDING)
        serialized_applications = ApplicationSerializer(applications, many=True)
        return Response(serialized_applications.data)
    
    @action(detail=False, methods=['get'], url_path='accepted-applications')
    def accepted_applications(self):
        applications = Application.objects.filter(status=Application.Status.ACCEPTED)
        serialized_applications = ApplicationSerializer(applications, many=True)
        return Response(serialized_applications.data)
    
    @action(detail=False, methods=['get'], url_path='rejected-applications')
    def rejected_applications(self):
        applications = Application.objects.filter(status=Application.Status.REJECTED)
        serialized_applications = ApplicationSerializer(applications, many=True)
        return Response(serialized_applications.data)




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

#viewset to handle payments
class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


    def perform_create(self, serializer):
        applicant = Applicant.objects.get(user=self.request.user)
        serializer.save(applicant=applicant)
        return Response({"message": "Payment submitted successfully"})
    
    @action(detail=False, methods=['get'], url_path='my-payments')
    def my_payments(self, request):
        user = request.user
        applicant = Applicant.objects.get(user=user)
        payments = Payment.objects.filter(applicant=applicant)
        serialized_payments = PaymentSerializer(payments, many=True)
        return Response(serialized_payments.data)
    
    
    @action(detail=False, methods=['get'], url_path='payment-summary')
    def payment_summary(self, request):
        user = request.user
        applicant = Applicant.objects.get(user=user)
        payments = Payment.objects.filter(applicant=applicant)
        total_payments = payments.count()
        total_amount = sum(payment.ammount for payment in payments)
        summary = {
            "total_payments": total_payments,
            "total_amount": total_amount
        }
        return Response(summary)