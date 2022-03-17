"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from unicodedata import name
from django.contrib import admin
from django.urls import path
# from Login.views import login_view
from Login.views import profile_view
from Login.views import dashboard_view
from Mess.views import mess_view
from django.contrib.auth import views as auth_view
urlpatterns = [
    # path('qr',include('qrscan.urls')),
    path('admin/', admin.site.urls),
    path('login1/',auth_view.LoginView.as_view(template_name='login.html'),name='login1'),
    path('mess/',mess_view,name="mess_view"),
    path('profile/<int:id>',profile_view),
    path('dashboard/<int:id>',dashboard_view,name="dashboard"),
    path('api/',include('Mess.urls')),
