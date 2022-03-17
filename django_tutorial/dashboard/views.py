from django.shortcuts import render
from dashboard.models import CountryData


# Create your views here.
def dashboard(request):
    # 각 나라와 인구 숫자 가져오기
    data = CountryData.objects.all()
    # print(data)

    aaa = "대시보드 만들기"
    return render(request, 'dashboard/dashboard.html', {'dataset':data} )



# class CountryData(models.Model):
#     country = models.CharField(max_length=100)
#     population = models.IntegerField()