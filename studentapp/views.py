from django.shortcuts import render


def studenthomepage(request):
    return render(request,'studentapp/StudentHomePage.html')
