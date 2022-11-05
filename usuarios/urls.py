#importes de urls
from django.urls import path


# importes de views
from .views import  locationUpdate , locationList

urlpatterns = [
    #path('api/location/update/', LocationUpdate.as_view(), name='location'),
    path('api/location/list/', locationList, name='location'),
    path('api/location/update/<int:pk>/', locationUpdate, name='location'),
]
