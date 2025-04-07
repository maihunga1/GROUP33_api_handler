from django.shortcuts import render
import yfinance as yf
from django.http import JsonResponse
from datetime import datetime, timedelta
import json

def to_json_hourly(ticker):
    stock = yf.Ticker(ticker)

    hist_hourly = stock.history(period="7d", interval="1h")

    json_data_hist_hourly = hist_hourly.to_json(orient='records')

    json_data_hist_hourly = json.loads(json_data_hist_hourly)

    for idx, record in enumerate(json_data_hist_hourly):
        record['date'] = hist_hourly.index[idx]


    return ({
        ticker: {
            "hourly": json_data_hist_hourly,
    }})