#importes de urls
from django.urls import path

#importes de vistas
from .views import home ,  dashboard

urlpatterns = [
    #comentario de home
    path('', home.as_view(), name='home'),

    #comentario de dashboard
    path('dashboard/', dashboard.as_view(), name='dashboard'),

]
