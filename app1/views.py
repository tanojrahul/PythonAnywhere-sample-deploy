from django.shortcuts import render
from django.template.context_processors import request

from .models import Student

from django.shortcuts import render
from .models import Student

def student_list(request):
    students = Student.objects.all()  # Fetch all students

    # Get search and filter values from the request
    search_query = request.GET.get('search', '')
    branch_filter = request.GET.get('branch', '')
    gender=request.GET.get('gender','')
    # Filter by search query (name)
    if search_query:
        students = students.filter(name__icontains=search_query)

    # Filter by branch
    if branch_filter:
        students = students.filter(branch=branch_filter)
    if gender:
        students=students.filter(gender=gender)

    context = {
        'students': students,
    }

    return render(request, 'student_list.html', context)

from django.shortcuts import render, redirect
from .forms import StudentForm


def student_register(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  # Save form data to the database
            return redirect('success')  # Redirect to a success page (or any other page)
    else:
        form = StudentForm()

    return render(request, 'student_register.html', {'form': form})


def success(request):
    return render(request, 'success.html')


def home(request):
    return render(request, 'home.html')


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse


# User Login
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_superuser:
                return HttpResponse("Admins cannot log in here.")
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')


# Admin Login
def admin_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            return render(request, 'admin_login.html', {'error': 'Invalid credentials'})
    return render(request, 'admin_login.html')

# User Dashboard (Login Required)
@login_required
def user_dashboard(request):
    return render(request, 'user_dashboard.html')

# Admin Dashboard (Login Required)
@login_required
def admin_dashboard(request):
    if not request.user.is_superuser:
        return HttpResponse("You are not authorized to view this page.")
    users = User.objects.all()
    return render(request, 'admin_dashboard.html', {'users': users})

# Logout

def user_logout(request):
    logout(request)
    return redirect('home')


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


# User Registration
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after registration
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})

