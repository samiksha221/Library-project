"""books URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from .views import home,Student,student_list,addstudent,deletstudent,updatestudent,Book,book_list,deletebook,updatebook,addbook,issueBook,issuebook_list,updateissuebook,addissuebook,deleteissuebook,register

urlpatterns = [

    path('',home),
    path('student',Student),
    path('list',student_list),
    path('delete-student/<str:id>',deletstudent),
    path('update-student/<str:id>',updatestudent),
    path('add-student',addstudent),
    path('book',Book),
    path('lists',book_list),
    path('delete-book/<str:id>',deletebook),
    path('update-book/<str:id>',updatebook),
    path('add-book',addbook),
    path('issuebook', issueBook),
    path('listss', issuebook_list),
    path('delete-issuebook/<str:id>', deleteissuebook),
    path('update-issuebook/<str:id>', updateissuebook),
    path('add-issuebook', addissuebook),
    path('register',register)
]

