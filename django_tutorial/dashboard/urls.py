from django.urls import path
from .views import dashboard

app_name = "dashboard"
urlpatterns = [

    # 가운데는 클래스 명 및 함수 명 (#dashboard파일에서 가지고 와야함)
    path('', dashboard, name="dashboard"),


]
