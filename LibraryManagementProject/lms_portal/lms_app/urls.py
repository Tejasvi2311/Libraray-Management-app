"""
URL configuration for lms_portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include

from . import views
from .views import *


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('home', views.home,name='home'),
    path('home', home),
    path('add_book', add_book),
    path('add_book/add',save_book),
    path('search_book', search_book),
    path('search/', views.search_view, name='search_view'),
    path('issue_book/', issue_book, name='issue_book'),
    path('delete_book', delete_book),
    path('shop', shopping),
    path('save',save_student),
    path('books/', views.book_list, name='book_list'),  # URL for the book list view
    path('books/delete', views.deleting_book, name='deleting_book'),
    path('logout/', views.logout_view, name='logout'),

]
