"""django_bd_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django_bd_app import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/', views.lista_eventos),
    path('agenda/lista/', views.json_lista_evento),
    path('agenda/evento/', views.eventos),
    path('agenda/evento/submit', views.submit_evento),
    path('agenda/evento/delete/<int:id_evento>/', views.delete_evento),
    path('', RedirectView.as_view(url='/agenda/')),  
    path('hello/<nome>/<int:idade>', views.hello),
    path('soma/<int:num1>/<int:num2>/', views.soma),
    path('login/', views.login_user),
    path('login/submit', views.submit_login), #Por ser post não deve ter / depois do submit (/errado/submit/)
    path('logout/', views.logout_user)
]

#path('', RedirectView.as_view(url='/agenda/')), substituiu('', views.index),
#path('login/submit', views.submit_login), Por ser 'POST' não deve ter '/' depois do submit (/errado/submit/)
