from django.urls import path
from django.views import View 
from . import views

urlpatterns = [
    path('signup/' , views.signup , name ="signup"),  
     path('login/' , views.login , name ="login"),  
    
]
