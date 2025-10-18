from django.db import connection
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Car
from .serializer import CarSerializer

class CarListCreate(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    
    # pang Truncate sa table
    def delete(self, request, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute(f'DELETE FROM api_car;')
            cursor.execute(f'DELETE FROM sqlite_sequence WHERE name="api_car";')
        return Response(status=status.HTTP_204_NO_CONTENT)
 
class CarRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'pk'