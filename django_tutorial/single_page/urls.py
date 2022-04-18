from django.urls import path
from .views import index, aboutMe, profileCard

app_name = "single_page"
urlpatterns = [

    # /index
    path('', index, name="index"),

    # /aboutme
    path('aboutme/', aboutMe, name="aboutme"),

    # profile_card 추가
    path('profile_card/', profileCard, name="profile_card"),

]
