from django.shortcuts import render, redirect
from .models import (Trip, Company, Pass_in_trip, Passenger, GoodTypes, Goods,
                     FamilyMembers, Payments, Student, Class, Student_In_Class,
                     Timepair, Teacher, Subject, Schedule, Users, Rooms,
                     Reservations, Reviews, Assignments, Course, User)
from django.contrib import messages
import hashlib

# Create your views here.
def index(request):
    return render(request, 'index.html')

def tutorial(request):
    return render(request, 'course/tutorial.html')

def course(request):
    course = Course.objects.all()
    context = {'course': course }
    return render(request, 'course/course.html', context)

def simulator(request):
    assignments = Assignments.objects.all()
    context = {'assignments': assignments}
    return render(request, 'simulator.html', context)

def table_family(request):
    goodtypes = GoodTypes.objects.all()
    goods = Goods.objects.all()
    familymembers = FamilyMembers.objects.all()
    payments = Payments.objects.all()
    context = {
        'goodtypes': goodtypes,
        'goods': goods,
        'familymembers': familymembers,
        'payments': payments
    }
    return render(request, 'tab/table_family.html', context)

def table_schedule(request):
    student = Student.objects.all()
    klass = Class.objects.all()
    student_in_class = Student_In_Class.objects.all()
    timepair = Timepair.objects.all()
    teacher = Teacher.objects.all()
    subject = Subject.objects.all()
    schedule = Schedule.objects.all()
    context = {
        'student': student,
        'klass': klass,
        'student_in_class': student_in_class,
        'timepair': timepair,
        'teacher': teacher,
        'subject': subject,
        'schedule': schedule
    }
    return render(request, 'tab/table_schedule.html', context)

def table_airbnb(request):
    users = Users.objects.all()
    rooms = Rooms.objects.all()
    reservations = Reservations.objects.all()
    reviews = Reviews.objects.all()
    context = {
        'users': users,
        'rooms': rooms,
        'reservations': reservations,
        'reviews': reviews
    }
    return render(request, 'tab/table_airbnb.html', context)

def tables(request):
    trip = Trip.objects.all()
    company = Company.objects.all()
    pass_in_trip = Pass_in_trip.objects.all()
    passenger = Passenger.objects.all()

    context = {'trip': trip,
               'company': company,
               'pass_in_trip': pass_in_trip,
               'passenger': passenger}

    return render(request, 'tables.html', context)

def aviacompany_code(request):
    return render(request, 'tab/aviacompany_code.html')

def family_code(request):
    return render(request, 'tab/family_code.html')

def schedule_code(request):
    return render(request, 'tab/schedule_code.html')

def airbnb_code(request):
    return render(request, 'tab/airbnb_code.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        raw_password = request.POST['password']
        password = hashlib.sha256(raw_password.encode()).hexdigest()

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Пользователь уже существует')
            return redirect('register')
        if not any(char in '!№%?*' for char in raw_password):
            messages.error(request, 'Your password must contain symbols !№%?*')
            return redirect('register')
        if not any(char in '123456789' for char in raw_password):
            messages.error(request, 'Your password must contain numbers')
            return redirect('register')
        if len(raw_password) < 10:
            messages.error(request, 'Сome up with a stronger password')
            return redirect('register')
        if len(raw_password) > 50:
            messages.error(request, 'Password is too long. Max: 50')
            return redirect('register')


        User.objects.create(username=username, password=password)
        return redirect('welcome')
    return render(request, 'registrations/registrations.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        raw_password = request.POST['password']
        password = hashlib.sha256(raw_password.encode()).hexdigest()

        try:
            user = User.objects.get(username=username, password=password)
            request.session['user_id'] = user.id
            return redirect('index')
        except User.DoesNotExist:
            messages.error(request, 'Wrong data')
            return redirect('login')
    return render(request, 'registrations/login.html')

def logout_view(request):
    request.session.flush()
    return redirect('index')


def welcome_page(request):
    return render(request, 'registrations/welcome_page.html')

