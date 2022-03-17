from django.shortcuts import redirect, render
from dashboard.forms import CountryDataForm
from dashboard.models import CountryData


# Create your views here.
def dashboard(request):
    # 각 나라와 인구 숫자 가져오기
    data = CountryData.objects.all()


    # add 버튼 클릭, 값 입력 요청 처리
    if request.method == 'POST':
        # DB 입력
        form = CountryDataForm(request.POST)
        # 입력된 곳에 데이터가 담겨 있으면
        if form.is_valid():
            # 데이터 save
            form.save()
            return redirect(' . ')
    # form 출력
    else:
    # form 객체 생성
        form = CountryDataForm()
    # 랜더링 전달 데이터와 폼 객체 저장
    context = {'dataset':data, 'form' : form}
    return render(request, 'dashboard/dashboard.html', context)



# class CountryData(models.Model):
#     country = models.CharField(max_length=100)
#     population = models.IntegerField()