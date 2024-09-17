from django.shortcuts import render
from django.http import HttpResponse
from .forms import myform
from .models import mydb
# Create your views here.
def index(request):
    try:
        n1 = request.GET['fn']
        n2 = request.GET['fp']
        print('name:' + n1 )
        print('phone:' + n2 )
        n3 = mydb()
        n3.prodname = n1
        n3.prodphone = int(n2)
        n3.save()
    except:
        pass
    return render(request,'index.html')