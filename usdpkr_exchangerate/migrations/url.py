from django.urls import path
from . import views
from .views import simple_bar_chart

app_name = 'usdpkr_exchangerate'

urlpatterns = [
    path('home/', views.currency_convert, name='currency_converter'),
    path('prices/',views.simple_bar_chart, name='Bar_chart'),
    path('history/',views.display_csv, name="history"),
    path('average/',views.monthly_average, name="average"),
    path('average2/',views.moving_average, name="average2")
]
