from rest_framework import generics, filters
from .models import ContactUs
from .serializers import ContactUsSerializer

class ContactUsList(generics.ListCreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['email', 'message']

    def perform_create(self, serializer):
        email = self.request.data.get('email')
        message = self.request.data.get('message')
        if email and message:
            contact_us = ContactUs(email=email, message=message)
            contact_us.save()
            serializer.instance = contact_us
        else:
            raise serializers.ValidationError("Email and Message fields are required.")

class ContactUsDetail(generics.RetrieveUpdateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer