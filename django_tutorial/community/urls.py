from django.urls import path    
from community.views import *
    
app_name = "community"
urlpatterns=[
    path('write/', write, name = 'write'), #path, view의 함수
    path('list/', articleList, name="article_list"),
    # /view_detail/1/
    path('view_detail/<int:num>/', viewDetail, name='view_detail')
]