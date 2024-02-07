
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from.models import*
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group


def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def service(request):
    return render(request, "service.html")
    
@login_required
def dashboard(request):
    if request.method == 'POST':
        date = request.POST['date']
        message = request.POST['message']
        user = request.user

        new_appointment = Appointment(user=user, date=date, message=message)
        new_appointment.save()

        return redirect('dashboard')

    user_appointments = Appointment.objects.filter(user=request.user)
    all_appointments = Appointment.objects.all()
    
    return render(request, "dashboard.html", {'all_user_appointments': user_appointments, 'all_appointments': all_appointments})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = authenticate(request, username=username, password=password)
        except User.DoesNotExist:
            user = None 

        if user:
            print("Successfullllll")
            login(request, user)
            return redirect('dashboard')
        
    return render(request, "login.html")

def signup(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        
        username = firstname + '_' + lastname
        existing_user = User.objects.filter(username=username).first()

        if existing_user is not None:
            new_username = f'{username}_1'
            existing_user.username = new_username
            existing_user.save()
            return render(request, 'signup.html', {'response_content': 'Username already taken'})
        else:
            user = User.objects.create_user(username, email, password)
            user = authenticate(request, username=username, password=password)

            if user is not None:
                group_users = Group.objects.get(name='User')
                user.groups.add(group_users)
            else:
                return render(request, 'signup.html', {'response_content': 'Unable to authenticate'})

            if user:
                login(request, user)
                return redirect('dashboard')
            
    return render(request, "signup.html")
