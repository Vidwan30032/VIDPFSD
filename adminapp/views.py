from django.contrib.auth import authenticate
from django.shortcuts import render, redirect,get_object_or_404

# Create your views here.

def projecthomepage(request):
    return render(request,'adminapp/Projecthomepage.html')

def printpagecall(request):
    return render(request,'adminapp/printer.html')

def printpagelogic(request):
    if request.method == 'POST':
        user_input = request.POST['user_input']
        print(f"User Input: {user_input}")
    a1 = {'user_input':user_input}
    return render(request,'adminapp/printer.html',a1)

def exceptionpagecall(request):
    return render(request,'adminapp/ExceptionExample.html')

def exceptionpagelogic(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        result = None
        error_message = None
        try:
            num = int(user_input)
            result = 10/num
        except Exception as e:
            error_message = str(e)
        return render(request,'adminapp/ExceptionExample.html',{'result':result,'error':error_message})
    return render(request,'adminapp/ExceptionExample.html')

from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render

def UserRegisterCall(request):
    return render(request,'adminapp/UserRegisterPage.html')


def UserRegisterPageCall(request):
    return render(request, 'adminapp/UserRegisterPage.html')
def UserRegisterLogic(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return render(request, 'adminapp/UserRegisterPage.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'OOPS! Email already registered.')
                return render(request, 'adminapp/UserRegisterPage.html')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=pass1,
                    first_name=first_name,
                    last_name=last_name,
                    email=email

                )
                user.save()
                messages.info(request, 'Account created Successfully!')
                return render(request, 'adminapp/UserLoginPageCall.html')
        else:
            messages.info(request, 'Passwords do not match.')
            return render(request, 'adminapp/UserRegisterPage.html')
    else:
        return render(request, 'adminapp/UserRegisterPage.html')



def UserLoginCall(request):
    return render(request,'adminapp/UserLoginPageCall.html')

from .forms import *
from .models import Task

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_task')

    else:
        form = TaskForm()
    tasks = Task.objects.all()
    return render(request,'adminapp/add_task.html',{'form': form,'tasks':tasks})

def delete_task(request,pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('add_task')

def UserLoginPageCall(request):
    return render(request, 'adminapp/UserLoginPageCall.html')

def UserLoginLogic(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(request, username=username, password=password)


        if user is not None:
            auth.login(request, user)
            if len(username) == 10:
                # Redirect to StudentHomePage
                #messages.success(request, 'Login successful as student!')
                return redirect('studentapp:studenthomepage')  # Replace with your student homepage URL name
                # return render(request, 'facultyapp/FacultyHomepage.html')
            elif len(username) == 4:
                # Redirect to FacultyHomePage
                #messages.success(request, 'Login successful as faculty!')
                return redirect('facultyapp:facultyhomepage')  # Replace with your faculty homepage URL name
                # return render(request, 'facultyapp/FacultyHomepage.html')
            else:
                # Invalid username length
                messages.error(request, 'Username length does not match student or faculty criteria.')
                return render(request, 'adminapp/UserLoginPageCall.html')
        else:
            # If authentication fails
            messages.error(request, 'Invalid username or password.')
            return render(request, 'adminapp/UserLoginPageCall.html')
    else:
        return render(request, 'adminapp/UserLoginPageCall.html')

def logout(request):
    auth.logout(request)
    return redirect('projecthomepage')

def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("studentlist")
    else:
        form = StudentForm()
    return render(request,'adminapp/add_student.html',{'form':form})


def studentlist(request):
    students = StudentList.objects.all()
    return render(request,'adminapp/student_list.html',{'students':students})



def datetimepagecall(request):
    return render(request,'adminapp/datetimepage.html')


import datetime
from datetime import timedelta
import calendar


def datetimepagelogic(request):
    if request.method == "POST":
        number1 = int(request.POST['date1'])  # Get the number of days from the form input
        x = datetime.datetime.now()  # Get the current datetime
        ran = x + timedelta(days=number1)  # Add the number of days
        ran1 = ran.year  # Get the year from the resulting datetime

        # Use the calendar module to check if the year is a leap year
        ran2 = calendar.isleap(ran1)

        # Determine if it's a leap year or not
        if not ran2:
            ran3 = "Not a Leap Year"
        else:
            ran3 = "Leap Year"

        # Pass the values to the template
        a1 = {'ran': ran, 'ran3': ran3, 'ran1': ran1, 'number1': number1}
        return render(request, 'adminapp/datetimepage.html', a1)

    # Optional fallback if the request method isn't POST
    return render(request, 'adminapp/datetimepage.html')


import random,string
def randompagecall(request):
    return render(request,'adminapp/captcha.html')

def randomlogic(request):
    if request.method == "POST":
        number1 = int(request.POST['number1'])
        ran = ''.join(random.sample(string.ascii_uppercase + string.digits, k=number1))
    a1 = {'ran':ran}
    return render(request,'adminapp/captcha.html',a1)


from .models import feedback

def feedback_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')  # Fetch name from the POST request
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        textfield = request.POST.get('textfield')

        # Ensure that name (and other fields) are not empty
        if name and email and phonenumber and textfield:
            new_feedback = feedback(name=name, email=email, phonenumber=phonenumber, textfield=textfield)
            new_feedback.save()
            return render(request, 'adminapp/feedback.html', {'message': 'Feedback submitted successfully!'})
        else:
            return render(request, 'adminapp/feedback.html', {'error': 'All fields are required.'})

    return render(request, 'adminapp/feedback.html')



#c205