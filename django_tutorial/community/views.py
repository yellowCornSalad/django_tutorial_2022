from django.shortcuts import render
from community.forms import Form
from .models import Article
# Create your views here.

# 저장 소스코드
def write(request):
    if request.method == 'POST': # POST=> 코드보안
        form = Form(request.POST)
        if form.is_valid():
            form.save() # 필드값 저장함.
    # 빈 form페이지 요청
    else:
        form =Form()
    return render(request, 'write.html', {'form':form})

    # 글 작성 목록 보여주기
def articleList(request):
    article_list = Article.objects.all()
    return render(request, 'list.html', {'article_list': article_list})
    
def viewDetail(request, num=1):
    article_detail = Article.objects.get(id=num)
    # article_detail = get_object_or_404(Article, id=num)
    return render(request, 'view_detail.html', {'article_detail': article_detail})
