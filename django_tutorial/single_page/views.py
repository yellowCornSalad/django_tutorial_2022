from django.shortcuts import render
from community.models import Article


# Create your views here.
def index(request):  # 메모 남기기 index.html 페이지 구형
    latest_article_list = Article.objects.all().order_by('-cdate')[:3]
    return render(request, 'single_page/index.html', {'latest_article_list': latest_article_list})


def aboutMe(request):
    return render(request, 'single_page/aboutme.html',)


def profileCard(request):
    return render(request, 'single_page/profile_card.html',)
