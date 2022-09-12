"""config URL Configuration

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
from django.urls import path
from .views import *

urlpatterns = [
    path('', glavnaya, name='index'),
    path('books/add/', add_book, name='add-book'),
    path('books/view/<int:id>/', view_book, name='view-book'),
    path('books/delete/<int:id>/', delete_book, name='delete-book'),
    path('o-nas/', o_nas, name='o-nas'),
    path('manage/', manage, name='manage'),
    # path('example/', test_form_view, name='example'),
    path('publishers/', PublisherListView.as_view(), name='publishers'),
    path('publishers/create/', PublisherCreateView.as_view(), name='add-publisher'),
    path('publishers/view-publisher/<int:pk>/', PublisherDetialView.as_view(), name='detial-publisher'),
    path('publishers/update-publisher/<int:pk>/', PublisherUpdateView.as_view(), name='update-publisher'),
    path('publishers/delete-publisher/<int:pk>/', PublisherDeleteView.as_view(), name='delete-publisher'),
    path('login/',login_view,name ='login'),
    path('logout/', logout_request, name='logout'),
    path('register/', register_view, name='register'),
]
