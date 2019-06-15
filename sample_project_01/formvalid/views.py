from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from formvalid.forms import InsertDataForm, UpdateDataForm, DeleteDataForm
from formvalid.models import Student


def home_view(request):
    return render(request,'curd_home.html')

def insert_view(request):
    if request.method == 'POST':
        iform = InsertDataForm(request.POST)
        if iform.is_valid():
            rno = request.POST.get('rno')
            sname = request.POST.get('sname')
            category = request.POST.get('category')
            city = request.POST.get('city')
            result = request.POST.get('result')
            # photo = request.POST.get('photo')

            stdinfo = Student(rno = rno,
                              sname = sname,
                              category = category,
                              city = city,
                              result = result)
                              # photo = photo)
            stdinfo.save()
            iform = InsertDataForm()
            return render(request,'student_insert.html',{'iform':iform})
        else:
            return HttpResponse("<html>"
                            "<body><center><h1 color='red'>Invalid form</h1></center>"
                            "</body>"
                            "</html>")
    else:
        iform = InsertDataForm()
        return render(request,'student_insert.html',{'iform':iform})


def fetch_view(request):
    stdinfo = Student.objects.all()
    return render(request,'student_fetch.html',{'stdinfo':stdinfo})


def update_view(request):
    if request.method == 'POST':
        student_update = UpdateDataForm(request.POST)
        if student_update.is_valid():
            rno = request.POST.get('rno')
            result = request.POST.get('result')
            sdata = Student.objects.filter(rno=rno)
            if not sdata:
                return HttpResponse("Invalid Roll number")
            else:
                sdata.update(result = result)
                student_update = UpdateDataForm()
                return render(request,'student_update.html',{'student_update':student_update})
    else:
        student_update = UpdateDataForm()
        return render(request,'student_update.html',{'student_update':student_update})


def delete_view(request):
    if request.method == 'POST':
        student_delete = DeleteDataForm(request.POST)
        if student_delete.is_valid():
            rno = request.POST.get('rno','')
            stdinfo = Student.objects.filter(rno = rno)
            if not stdinfo:
                return HttpResponse("Roll number not avaliable")
            else:
                stdinfo.delete()
                student_delete = DeleteDataForm()
                return render(request,'student_delete.html',{'student_delete':student_delete})
    else:
        student_delete =DeleteDataForm()
        return render(request,'student_delete.html',{'student_delete':student_delete})