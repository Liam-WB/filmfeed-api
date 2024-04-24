from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ContactMessage
from .serializers import ContactFormSerializer

@api_view(['GET', 'POST'])
def contact_form(request):
    if request.method == 'GET':
        serializer = ContactFormSerializer()
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ContactFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
