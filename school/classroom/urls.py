from django.urls import path
from . import views

app_name = 'classroom'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('thank_you/', views.ThankYou.as_view(), name='thank_you'),
    path('contact/', views.ContactFormView.as_view(), name='contact')
]