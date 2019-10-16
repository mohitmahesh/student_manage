from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import StudentDetails
from .models import Term1
from .models import Term2
from .models import Finals
from .models import User
from django.contrib.auth import authenticate,get_user_model,login,logout

def base(request):
    return render(request, 'base.html')

def login_s(request):
    if request.method == 'POST':
        data = request.POST
        username = data['username']
        password = data['password']
        student = authenticate(username=username,password=password)
        if student is None:
            return redirect('login')
        else:
            login(request,student)
            return redirect('home')
    return render(request,"login.html")

def login_t(request):
    if request.method=="POST":
        data=request.POST
        username = data['username']
        password = data['password']
        teacher=authenticate(username=username,password=password)
        if teacher is None:
            return redirect('logintea')
        else:
            logintea(request,teacher)
            return redirect('hometea')
    return render(request,"logintea.html")

def home(request):
    user = request.user
    student_id = user.id
    #username=form.cleaned_data.get('username')
    student_object = User.objects.get(id=student_id)
    student_details = StudentDetails.objects.get(user=student_object)
    return render(request,'home.html',{'student':student_details})
    
@login_required(login_url='s_manage:login')
def logout_view(request):
    logout(request)
    return redirect('myaccounts:home')


@login_required    
def term1(request):
    student = request.user
    student_id = student.id
    student_object = User.objects.get(id=student_id)
    student_details = StudentDetails.objects.get(user=student_object)
    term1_marks = Term1.objects.get(user=student_details)
    return render(request, 'marks.html', {'marks':term1_marks})
@login_required
def term2(request):
    student = request.user
    student_id = student.id
    student_object = User.objects.get(id=student_id)
    student_details = StudentDetails.objects.get(user=student_object)
    term2_marks = Term2.objects.get(user=student_details)
    return render(request, 'marks.html', {'marks':term2_marks})
@login_required
def finals(request):
    student = request.user
    student_id = student.id
    student_object = User.objects.get(id=student_id)
    student_details = StudentDetails.objects.get(user=student_object)
    finals_marks = Finals.objects.get(user=student_details)
    return render(request, 'marks.html', {'marks':finals_marks})

@login_required
def reportcard(request):
    student = request.user
    student_id = student.id
    student_object = User.objects.get(id=student_id)
    student_details = StudentDetails.objects.get(user=student_object)
    term1_marks = Term1.objects.get(user=student_details)
    term2_marks = Term2.objects.get(user=student_details)
    finals_marks = Finals.objects.get(user=student_details)
    return render(request,'reportcard.html', {'term1_marks':term1_marks,'term2_marks':term2_marks,'finals_marks':finals_marks})