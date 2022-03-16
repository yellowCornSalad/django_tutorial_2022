from django.shortcuts import *
from community.forms import Form
from .models import *
# Create your views here.

# 저장 소스코드
def write(request):
    if request.method == 'POST': # POST=> 코드보안
        form = Form(request.POST)
        if form.is_valid():
            form.save() # 필드값 저장함.
            return redirect('.') # 새로고침했을때 데이터들 꺠끗하게 지워줌
    # 빈 form페이지 요청
    else:
        form =Form()
    return render(request, 'write.html', {'form':form})

    # 글 작성 목록 보여주기
def articleList(request):
    article_list = Article.objects.all()
    return render(request, 'list.html', {'article_list': article_list})
    
def viewDetail(request, num=1):
    # article_detail = Article.objects.get(id=num) # id 대신 pk도 가능
    article_detail = get_object_or_404(Article, pk=num) # 존재하지 않는 쪽수 입력시 404츨력
    return render(request, 'view_detail.html', {'article_detail': article_detail})
def index(request): # 메모 남기기 index.html 페이지 구형
    latest_article_list = Article.objects.all().order_by('-cdate')[:3]
    return render(request, 'index.html', {'latest_article_list': latest_article_list})