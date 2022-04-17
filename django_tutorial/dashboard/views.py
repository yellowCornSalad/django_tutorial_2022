from bs4 import BeautifulSoup as BS
import requests
from django.shortcuts import render
# from django.shortcuts import redirect, render
from dashboard.forms import CountryDataForm
from dashboard.models import CountryData


# Create your views here.

# Create your views here.

def dashboard(request):  # 코드 구현
    temp = request.POST.get('message')
    url = 'http://openapi.kepco.co.kr/service/EvInfoServiceV2/getEvSearchList'
    params = {'serviceKey': 'xcjmOs938MfzLWnUORs6dWmmxjKPXykAsj/r2u/JdDMCJqQeEvfhXCK+DWAIqGY4BShHzUzFRQqoSzAOMGZXzg==',
              'pageNo': '1', 'numOfRows': '50', 'addr': temp}
    response = requests.get(url, params=params)
    soup = BS(response.text, 'html.parser')

    pc = []
    num = 1
    items = soup.find_all('item')
    for i in items:
        temp = []
        a = float(i.find('lat').text)
        b = float(i.find('longi').text)
        c = int(i.find('cpstat').text)
        if(c == 1):
            c = "충전가능"
        elif(c == 2):
            c = "충전중"
        elif(c == 3):
            c = "고장/점검"
        elif(c == 4):
            c = "통신장애"
        else:
            c = "통신미연결"
        d = i.find('addr').text
        e = i.find('csnm').text
        f = int(i.find('chargetp').text)
        if(f == 1):
            f = "완속"
        elif(f == 2):
            f = "급속"
        temp.append(a)
        temp.append(b)
        temp.append(c)
        temp.append(d)
        temp.append(e)
        temp.append(f)
        temp.append(num)
        pc.append(temp)
        num += 1

    return render(request, "dashboard/dashboard.html", {'pc': pc})
