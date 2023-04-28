"""
URL configuration for sample_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from candidates import views

urlpatterns = [
    path('',views.Home_Page,name='Home_Page'),
    path('Dashboard',views.DASHBOARD,name = 'Dashboard'),
    path('Payment',views.Payment_Page,name = 'Payment'),
    path('SignUp_page',views.SignUp_Page,name='SignUp_Page'),
    path('Login_Page',views.Login_Page,name = 'Login_Page'),
    path('Allotment',views.Allotment,name = 'Allotment'),
    path('Attendance_Page',views.Attendance_Page,name = 'Attendance_Page'),
    path('vr',views.VR,name = 'vr'),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL,
                      document_root = settings.MEDIA_ROOT)
