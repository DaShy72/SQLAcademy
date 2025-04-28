from django.db import models


# This is model Avialines
class Trip(models.Model):
    id_trip = models.IntegerField(primary_key=True)
    company = models.ForeignKey('Company',
                                on_delete=models.CASCADE,
                                help_text='Company name')
    plane = models.CharField(max_length=30,
                             help_text='plane',)
    town_from = models.CharField(max_length=30,
                                 help_text='Input town from')
    town_to = models.CharField(max_length=30,
                               help_text='Input town to')
    time_out = models.DateTimeField()
    time_in = models.DateTimeField()

    def __str__(self):
        return self.company

class Company(models.Model):
    name = models.CharField(max_length=30,
                            help_text='Company name')
    def __str__(self):
        return self.name

class Pass_in_trip(models.Model):
    trip = models.ForeignKey('Trip',
                             on_delete=models.CASCADE,
                             help_text='Input trip id')
    passenger = models.ForeignKey('Passenger',
                                  on_delete=models.CASCADE,
                                  help_text='Input passenger')
    place = models.CharField(max_length=5,
                             help_text='Place client')
    def __str__(self):
        return self.trip

class Passenger(models.Model):
    name = models.CharField(max_length=30,
                            help_text='Passenger in trip')
    def __str__(self):
        return self.name



# This is group model Family

class GoodTypes(models.Model):
    good_type_id = models.IntegerField(primary_key=True)
    good_type_name = models.CharField(max_length=50)

    def __str__(self):
        return self.good_type_name

class Goods(models.Model):
    good_id = models.IntegerField(primary_key=True)
    good_name = models.CharField(max_length=50)
    type = models.ForeignKey('GoodTypes',
                             on_delete=models.CASCADE)
    def __str__(self):
        return self.good_name

class FamilyMembers(models.Model):
    member_id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=50)
    member_name = models.CharField(max_length=30)
    birthday = models.DateField()

    def __str__(self):
        return self.member_name

class Payments(models.Model):
    payment_id = models.IntegerField(primary_key=True)
    family_member = models.ForeignKey('FamilyMembers',
                                      on_delete=models.CASCADE)
    good = models.ForeignKey('Goods',
                             on_delete=models.CASCADE)
    amount = models.IntegerField()
    unit_price = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return self.family_member



# model group schedule

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField()
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.last_name

class Class(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Student_In_Class(models.Model):
    klass = models.ForeignKey('Class',
                              on_delete=models.CASCADE)
    student = models.ForeignKey('Student',
                              on_delete=models.CASCADE)
    def __str__(self):
        return self.klass

class Timepair(models.Model):
    start_pair = models.TimeField()
    end_pair = models.TimeField()

class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.last_name

class Subject(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Schedule(models.Model):
    date = models.DateField()
    klass = models.ForeignKey('Class',
                              on_delete=models.CASCADE,
                              verbose_name='class')
    number_pair = models.ForeignKey('Timepair',
                              on_delete=models.CASCADE)
    teacher = models.ForeignKey('Teacher',
                              on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject',
                              on_delete=models.CASCADE)
    classroom = models.IntegerField()

    def __str__(self):
        return self.classroom



# model group airbnb

class Users(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    email_verified_at = models.DateTimeField()
    password = models.CharField(max_length=70)
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return self.name

class Rooms(models.Model):
    home_type = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    has_tv = models.BooleanField()
    has_internet = models.BooleanField()
    has_kitchen = models.BooleanField()
    has_air_con = models.BooleanField()
    price = models.IntegerField()
    owner_id = models.ForeignKey('Users',
                                 on_delete=models.CASCADE)
    latitude = models.FloatField()
    longnitude = models.FloatField()

    def __str__(self):
        return self.home_type

class Reservations(models.Model):
    user = models.ForeignKey('Users',
                                on_delete=models.CASCADE)
    room = models.ForeignKey('Rooms',
                                on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    price = models.IntegerField()
    total = models.IntegerField()

class Reviews(models.Model):
    reservation = models.ForeignKey('Reservations',
                                    on_delete=models.CASCADE)
    rating = models.IntegerField()


class Assignments(models.Model):
    assignment_name = models.CharField(max_length=500)
    complexity = models.CharField(max_length=20)
    name_table = models.CharField(max_length=20)

    def __str__(self):
        return self.assignment_name


class Course(models.Model):
    text = models.CharField(max_length=100)
    chapter = models.IntegerField()

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=255)































