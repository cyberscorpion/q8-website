from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [

    path('', TemplateView.as_view(template_name='home.html')),
    path('about-us', TemplateView.as_view(template_name='about-us.html')),
    path('services', TemplateView.as_view(template_name='services.html')),
    path('services-1', TemplateView.as_view(template_name='services-1.html')),
    path('services-2', TemplateView.as_view(template_name='services-2.html')),
    path('services-3', TemplateView.as_view(template_name='services-3.html')),

]