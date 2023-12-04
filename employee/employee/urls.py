"""
URL configuration for employee project.

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
from work.views import Employee
from work.views import bookview
from work.views import moviesview
from work.views import Booklist
from work.views import Personview,Book_detailView,Mobileview,Studentview,studentDetailView,Book_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path("add/",Employee.as_view()),
    path("book/",bookview.as_view()),
    path("movie/",moviesview.as_view()),
    path("book/all/",Booklist.as_view(),name='book-al'),
    path("person/",Personview.as_view()),
    path("books/<int:pk>",Book_detailView.as_view(),name='book-det'),
    path("mobile/",Mobileview.as_view()),
    path("student/",Studentview.as_view()),
    path("students/<int:pk>",studentDetailView.as_view()),
    path("books/<int:pk>/remove",Book_delete.as_view(),name='book-del')
]
