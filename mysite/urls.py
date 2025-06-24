"""
URL configuration for mysite project.

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
from usdpkr_exchangerate.migrations import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.currency_convert, name='currency_converter'),
    path('prices/',views.simple_bar_chart, name='Bar_chart'),
    path('history/',views.display_csv, name="history"),
    path('average/',views.monthly_average, name="average"),
    path('average2/',views.moving_average, name="average2"),
]
