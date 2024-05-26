from.import views
from django.urls import path


urlpatterns = [
    
    path('student_register/',views.student_register,name='student_register'),
    path('student_login/',views.student_login,name='student_login'),
    path('student_logout/',views.student_logout,name='student_logout'),
    path('student_dashboard/',views.student_dashboard,name='student_dashboard'),
    path('python_course/',views.python_course,name='python_course'),
    path('fullstack_course/',views.fullstack_course,name='fullstack_course'),
    path('all_course/',views.all_course,name='all_course'),
    path('upload/', views.certificate_upload, name='certificate_upload'),
    
]
