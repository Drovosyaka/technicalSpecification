"""
URL configuration for technicalSpecification project.

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
from apiTechnicalSpecification.views import *
from appTechnicalSpecification.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/equipment/', EquipmentApiList.as_view()),
    path('api/equipment/<int:pk>/', EquipmentApiDetailView.as_view()),
    path('api/equipment-type/', EquipmentTypeApiList.as_view()),
    path('api/equipment-type/<int:pk>/', EquipmentTypeApiDetailView.as_view()),
    path('', mainPage, name='home'),
    path('search/<int:pk>/update/', EquipmentUpdate.as_view(), name='update'),
    path('search/<int:pk>/delete/', EquipmentDelete.as_view(), name='delete'),
    path('add/', create, name='add'),
]
