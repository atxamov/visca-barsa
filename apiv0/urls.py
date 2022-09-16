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
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from rest_framework import routers

router = routers.SimpleRouter()

router.register(r'publishers', PublisherViewSet)
router.register(r'book', BookViewSet)
router.register(r'journalist', JournalistViewSet)
router.register(r'mananger', ManangerViewSet)
router.register(r'national', NationalTViewSet)

urlpatterns = [
    # Auth part    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # Loading and Download data from excell
    path('load-data-excel/', load_data_excell, name='load-data-excel'),

] + router.urls
