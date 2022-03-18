from django.urls import path    
from .views import index, aboutMe
    
app_name = "single_page"  
urlpatterns=[
    
    # /index
    path('', index, name="index"), 
    
    # /aboutme
    path('aboutme/', aboutMe, name="aboutMe"), 
]