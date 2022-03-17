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
        # 폼에 입력한 나라
        input_country = form.data.get('country', None)
        # 폼에 입력한 인구 수
        input_num = form.data.get('population', None)
        # 입력된 곳에 데이터가 담겨 있으면
        if form.is_valid():
            # DB안의 나라 이름이 중복 된 경우 업데이트
            # 아닌 경우, 나라 이름 추가
            # CRUD: Create, Read, Update, Delete
            CountryData.objects.update_or_create(
                # filter => 유/무 체크 => 입력한 나라이름이 이미 존재하는 나라 이름과 같으면(이미 존재하는 나라이름이면)
                country = input_country, 
                # new value => 추가
                # default 값은 form에 입력한 값임, d비버에서 맨위에 목록값인 country와 population을 위함.
                defaults = {
                    'country': input_country,
                    'population': input_num
                }
            )

            # 데이터 save
            # form.save()
            return redirect('.')
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