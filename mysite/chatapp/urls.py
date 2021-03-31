from django.contrib import admin
from django.urls import path,include
from . import views
from .views import home_view,ContactUsView

urlpatterns = [
    # path('home_view/', home_view.as_view(), name="HomeView"),
    path('home_view/', home_view, name="HomeView"),
    path('contact_view/', ContactUsView.as_View(), name="ContactUsView"),
]