# importes de rest_framework
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response import Response

#importes de models
from .models import Location
#importes de serializers
from .serializers import LocationUpdateSerializer

#importe de configuracion de la base de datos
from django.conf import settings 

import math

'''class LocationUpdate(UpdateAPIView):
    
    #clase para reescribir los datos de la ubicacion

    #serializador
    serializer_class = LocationUpdateSerializer
    queryset = Location.objects.all()'''



    

@api_view(['GET'])
def locationList(request):

    if request.method == 'GET':
        #consulta de la base de datos utilizando 
        queryset = Location.objects.filter(
                Location.lat >= 1
            )
        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        print(queryset)
        serializer = LocationUpdateSerializer(queryset, many=True)
        return Response(serializer.data)
    

    

@api_view(['PUT'])
def locationUpdate(request,pk):
    if request.method == 'PUT':
        queryset = Location.objects.filter(id=pk).first()
        serializer = LocationUpdateSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)