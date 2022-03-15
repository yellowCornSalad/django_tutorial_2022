from django.shortcuts import render

# Create your views here.
def write(request):
    render(request, "write.html")