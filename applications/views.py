from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser

from admit.models import Applicant, Application
from .serializers import ApplicantSerializer, ApplicationSerializer, TestimonialSerializer

class ApplicantsViewSet(ModelViewSet):
    """ViewSet for managing applicants.
    """
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer

    def perform_create(self, serializer):
        serializer.save()
        return Response({"message": "Applicant created successfully"})

class ApplicationsViewSet(ModelViewSet):
    """ViewSet for managing applications.
    """
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def perform_create(self, serializer):
        """Custom action to create an application for the logged-in user."""
        serializer.save()
        return Response({"message": "Application submitted successfully"})
    
    #custom action to view applications made by the logged-in user
    @action(detail=False, methods=['get'], url_path='my-applications')
    def my_applications(self, request):
        """Custom action to view applications made by the logged-in user."""
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
