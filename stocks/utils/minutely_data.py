from django.shortcuts import render
import yfinance as yf
from django.http import JsonResponse
from datetime import datetime, timedelta
import json


def to_json_minutely(ticker):
    stock = yf.Ticker(ticker)

    hist_minutely = stock.history(period="1d", interval="5m")

    json_data_hist_minutely = hist_minutely.to_json(orient='records')

    json_data_hist_minutely = json.loads(json_data_hist_minutely)

    for idx, record in enumerate(json_data_hist_minutely):
        record['date'] = hist_minutely.index[idx]

    return ({
        ticker: {
            "minutely": json_data_hist_minutely
    }})