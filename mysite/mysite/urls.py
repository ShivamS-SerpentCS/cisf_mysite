"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.homehtml),
    path('',views.index),
    path('appointment/',views.make_appointment),
    path('home_dark/',views.home_dark),
    path('about/',views.about),
    path('service/',views.service),
    path('service_list/',views.service_list),
    path('service_detail/',views.service_detail),
    path('blog/',views.blog),
    path('blog_grid/',views.blog_grid),
    path('blog_detail/',views.blog_detail),
    path('career/',views.career),
    path('price/',views.price),
    path('faq/',views.faq),
    path('shop_detail/',views.shop_detail),
    path('contact/',views.contact),
    path('term_condition/',views.term_condition),
    path('privacy_policy/',views.privacy_policy),
    path('news/',views.news),

]
