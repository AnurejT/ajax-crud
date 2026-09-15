"""
URL configuration for ajax2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from myapp import views

urlpatterns = [
    path('homepage_get/', views.homepage_get),
    path('addcontact_get/', views.addcontact_get),
    path('addcontact_post/', views.addcontact_post),
    path('contactbook_get/', views.contactbook_get),
    path('contactbook_get2/', views.contactbook_get2),
    path('editcontact_get/<id>', views.editcontact_get),
    path('editcontact_post/', views.editcontact_post),
    path('deletecontact_post/<id>/', views.deletecontact_post),
]
