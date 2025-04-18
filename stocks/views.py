from django.shortcuts import render
import yfinance as yf
from django.http import JsonResponse
from datetime import datetime, timedelta
import json
from .utils.daily_data import to_json_daily
from .utils.hourly_data import to_json_hourly
from .utils.minutely_data import to_json_minutely
from .utils.monthly_data import to_json_monthly
from .utils.yearly_data import to_json_yearly



tickers = ['CBA.AX', 'BHP.AX', 'CSL.AX', 'WBC.AX', 'NAB.AX']

def get_stock_data(ticker, interval, period):
    stock = yf.Ticker(ticker)
    # Fetch data with the given interval and period
    data = stock.history(period=period, interval=interval)
    # Convert to JSON and add the date as a column
    data['date'] = data.index
    return data.to_dict(orient="records")

def daily_all(request):
    daily_data = {}

    for ticker in tickers:
        data = to_json_daily(ticker)
        if data and ticker in data:
            daily_data[ticker] = data[ticker]["daily"]

    return JsonResponse(daily_data, safe=False)

def daily(request, ticker):
    data = to_json_daily(ticker)
    return JsonResponse(data, safe=False)

def hourly_all(request):
    hourly_data = {}

    for ticker in tickers:
        data = to_json_hourly(ticker)
        if data and ticker in data:
            hourly_data[ticker] = data[ticker]["hourly"]

    return JsonResponse(hourly_data, safe=False)

def hourly(request, ticker):
    data = get_stock_data(ticker, "1h", "7d")
    return JsonResponse(data, safe=False)

def minutely_all(request):
    minutely_data = {}

    for ticker in tickers:
        data = to_json_minutely(ticker)
        if data and ticker in data:
            minutely_data[ticker] = data[ticker]["minutely"]

    return JsonResponse(minutely_data, safe=False)

def minutely(request, ticker):
    data = get_stock_data(ticker, "5m", "1d")
    return JsonResponse(data, safe=False)


def monthly_all(request):
    monthly_data = {}

    for ticker in tickers:
        data = to_json_monthly(ticker)
        if data and ticker in data:
            monthly_data[ticker] = data[ticker]["monthly"]

    return JsonResponse(monthly_data, safe=False)

def monthly(request, ticker):
    data = get_stock_data(ticker, "1mo", "2y")
    return JsonResponse(data, safe=False)

def yearly_all(request):
    yearly_data = {}

    for ticker in tickers:
        data = to_json_yearly(ticker)
        if data and ticker in data:
            yearly_data[ticker] = data[ticker]["yearly"]

    return JsonResponse(yearly_data, safe=False)

def yearly(request, ticker):
    data = get_stock_data(ticker, "3mo", "15y")
    return JsonResponse(data, safe=False)