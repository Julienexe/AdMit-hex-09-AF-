from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from .models import School, Applicant, Payment
from .serializers import SchoolSerializer, PaymentSerializer


class SchoolsViewSet(ModelViewSet):
    """ViewSet for managing schools.
    """
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    def perform_create(self, serializer):
        serializer.save()
        return Response({"message": "School created successfully"})


#viewset to handle payments
class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    #only allow authenticated users to create payments, including jwt authentication


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