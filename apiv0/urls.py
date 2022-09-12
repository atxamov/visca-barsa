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
    path('books/', BookListAPIView.as_view(), name='get-books'),
    path('books/create/', BookCreateAPIView.as_view(), name='create-book'),
    path('books/get-update-delete/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='update-book'),
    path('publisher/', PublisherListAPIView.as_view(), name='get-publisher'),
    path('publisher/create/', PublisherCreateAPIView.as_view(), name='create-publisher'),
    path('publisher/get-update-delete/<int:pk>/', PublisherRetrieveUpdateDestroyAPIView.as_view(), name='update-publisher'),
    path('jurnalist/', JurnalistListAPIView.as_view(), name='get-jurnalist'),
    path('jurnalist/create/', JurnalistCreateAPIView.as_view(), name='create-jurnalist'),
    path('jurnalist/get-update-delete/<int:pk>/', JurnalistRetrieveUpdateDestroyAPIView.as_view(), name='update-jurnalist'),
    path('mananger/', ManangerListAPIView.as_view(), name='get-mananger'),
    path('mananger/create/', ManangerCreateAPIView.as_view(), name='create-mananger'),
    path('mananger/get-update-delete/<int:pk>/', ManangerRetrieveUpdateDestroyAPIView.as_view(), name='update-mananger'),
]
