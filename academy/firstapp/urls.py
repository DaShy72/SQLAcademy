from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tutorial/', views.tutorial, name='tutorial'),
    path('course/', views.course, name='course'),
    path('simulator/', views.simulator, name='simulator'),
    path('tables/', views.tables, name='tables'),
    path('aviacompany_code/', views.aviacompany_code, name='aviacompany_code'),
    path('family_code/', views.family_code, name='family_code'),
    path('schedule_code/', views.schedule_code, name='schedule_code'),
    path('airbnb_code/', views.airbnb_code, name='airbnb_code'),
    path('table_schedule', views.table_schedule, name='table_schedule'),
    path('table_family', views.table_family, name='table_family'),
    path('table_airbnb', views.table_airbnb, name='table_airbnb'),
    path('register/', views.register, name='register'),
    path('login_view/', views.login_view, name='login'),
    path('logout_view', views.logout_view, name='logout'),
    path('welcome_page/', views.welcome_page, name='welcome'),


]