from django.urls import path
from. import views

urlpatterns = [
    path('student_list',views.student_list,name='student_list'),
    path('register/', views.student_register, name='student_register'),
    path('success/', views.success, name='success'),
    path('', views.home, name='home'),
    path('login/', views.user_login, name='user_login'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('logout/', views.user_logout, name='logout'),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('register1/', views.register, name='register'),  # Add this line for registration

]
