from django.shortcuts import render

#importes vistas genericas
from django.views.generic import TemplateView

# Create your views here.


class home(TemplateView):
    template_name = 'index.html'


class dashboard(TemplateView):
    template_name = 'dashboard.html'