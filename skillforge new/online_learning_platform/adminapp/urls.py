from.import views
from django.urls import path


urlpatterns = [
    path('',views.home,name='home'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('courses/',views.courses,name='courses'),
    path('contact/',views.contact,name='contact'),
    path('courses_icon/',views.courses_icon,name='courses_icon'),
    
]
