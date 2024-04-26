from rest_framework import serializers
from .models import ContactUs

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ['id', 'name', 'email', 'message', 'created_at']
        read_only_fields = ['created_at']
