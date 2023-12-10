from django.urls import path
from . import views

urlpatterns=[
    path('home', views.home, name='home'),
    path('', views.login, name='login'),
    path('register', views.register, name='register'),
    path('complaint_list', views.complaint_list, name='complaint_list'),
    path('submit_complaint', views.submit_complaint, name='submit_complaint'),
    path('complaint_submitted', views.complaint_submitted, name='complaint_submitted'),
    
]