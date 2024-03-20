from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Team


def demo(request):
    obj = Place.objects.all()
    teams=Team.objects.all()
    return render(request, "index.html", {'result': obj, 'result2':teams})
















# def about(request):
#     x="india"
#     return render(request,"about.html",{'key1':x})
# def contact(request):
#     return HttpResponse("contact me...")
# def detail(request):
#     return render(request,"detail.html")
# def thanks(request):
#     return HttpResponse("thanks for your visit")
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     return render(request,"")
