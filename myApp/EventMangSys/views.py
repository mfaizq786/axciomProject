from django.shortcuts import render


# Create your views here.
def index(request):
    if request.POST:
        admin_name = request.POST.get('adminname')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        catagory = request.POST.get('catogory')

    return render(request,'EventMangSys\index.html')