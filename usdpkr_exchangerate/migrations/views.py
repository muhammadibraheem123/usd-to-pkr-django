# the comments in this program are used to describe what the functions do
# this program can be further used for other practice projects just for better understanding at how python and its functions works
from django.shortcuts import render
from django.views import generic
from usdpkr_exchangerate.models import ExchangeRate
import csv
import pandas as pd
import os
from django.conf import settings

def monthly_average(request):
    file_path = settings.BASE_DIR / 'mysite/USD_PKR_Exchange_Rate (1).csv'

    df = pd.read_csv(file_path)

    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.month
    month_average = df
    # month_average = df.groupby('Month')['USD_to_PKR'].mean().reset_index()

    status_labels = month_average['Month'].astype(str).tolist()
    month_average['Percentage_Change'] = month_average['USD_to_PKR'].pct_change() * 100
    status_count = month_average['Percentage_Change'].round(2).fillna(0).tolist()


    return render(request,'monthly_average.html',{
        'status_labels': status_labels,
        'status_count': status_count,
    })

def moving_average(request):
    file_path = settings.BASE_DIR / 'mysite/USD_PKR_Exchange_Rate (1).csv'

    df = pd.read_csv(file_path)

    df['Date'] = pd.to_datetime(df['Date'])
    df['YearMonth'] = df['Date'].dt.month
    month_average = df
    # month_average = df.groupby('YearMonth')['USD_to_PKR'].mean().reset_index()
    # month_average['YearMonth'] = month_average['YearMonth'].astype(str)

    #month moving average apply kar rahe hain
    month_average['Moving_Avg'] = month_average['USD_to_PKR'].rolling(window=3).mean() #the roling function is a functiom from pandas which is known for calculating moving average
    #the window arguement is used because we were supposed to calculat ethe average between 3 months


    status_labels = month_average['YearMonth'].tolist()
    actual_values = month_average['USD_to_PKR'].round(2).tolist() #the round(2) function rounds each numerical element in the array or Series to two decimal places
    # the .tolist() is  a method of NumPy arrays that returns a list representation of the array


    moving_avg_values = month_average['Moving_Avg'].round(2).fillna(0).tolist() #The fillna(0) function in Pandas replaces all missing or "Not a Number" (NaN) values within a DataFrame or Series with the numerical value 0


    return render(request, '3_month_average.html', {
        'status_labels': status_labels,
        'actual_values': actual_values,
        'moving_avg_values': moving_avg_values,
    })

def simple_bar_chart(request):
    # yahan par mai ne path ko string ki tarf direct kiya hai
    file_path = settings.BASE_DIR / 'mysite/USD_PKR_Exchange_Rate (1).csv'

    df = pd.read_csv(file_path)

    # date column ko datatime mai convert kiya hai aur year ko extract kiya hai takeh python is ko actual date ki tarha recoginize kar sake
    df['Date'] = pd.to_datetime(df['Date'])
    df['Year'] = df['Date'].dt.year

    # avg nikal rahe hain years ko group kar ke seekhta seekhta
    yearly_avg = df.groupby('Year')['USD_to_PKR'].mean().reset_index()

    status_labels = yearly_avg['Year'].astype(str).tolist()
    status_count = yearly_avg['USD_to_PKR'].round(2).tolist()


    return render(request, 'bar chart.html', {
        'status_labels': status_labels,
        'status_count': status_count,
    })

def display_csv(request):
    file_path = os.path.join(settings.BASE_DIR, 'mysite', 'USD_PKR_Exchange_Rate (1).csv')
    with open(file_path, newline='') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    return render(request, 'money_exchangerate_detail.html', {'data': data})

def currency_convert(request):
    EXCHANGE_RATE = 283

    context = {}

    if 'usd_to_pkr' in request.POST:
        usd = float(request.POST.get('usd_amount', 0))
        context['converted_pkr'] = round(usd * EXCHANGE_RATE, 2)
        context['usd'] = usd

    elif 'pkr_to_usd' in request.POST:
        pkr = float(request.POST.get('pkr_amount', 0))
        context['converted_usd'] = round(pkr / EXCHANGE_RATE, 2)
        context['pkr'] = pkr

    return render(request, 'index.html', context)


class MoneyList(generic.ListView):
    queryset = ExchangeRate.objects.order_by("data_created")
    template_name = "./templates/index.html"

class MoneyExchangeRateDetail(generic.DetailView):
    model = ExchangeRate
    template_name = "money_exchangerate_detail.html"