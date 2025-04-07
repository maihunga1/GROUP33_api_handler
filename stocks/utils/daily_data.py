from django.shortcuts import render
import yfinance as yf
from django.http import JsonResponse
from datetime import datetime, timedelta
import json

def to_json_daily(ticker):
    stock = yf.Ticker(ticker)
    end_date = datetime.today().strftime('%Y-%m-%d')
    start_date = (datetime.today() - timedelta(days=30)).strftime('%Y-%m-%d')

    hist_daily = stock.history(start=start_date, end=end_date, interval="1d")

    json_data_hist_daily = hist_daily.to_json(orient='records')

    json_data_hist_daily = json.loads(json_data_hist_daily)

    for idx, record in enumerate(json_data_hist_daily):
        record['date'] = hist_daily.index[idx]

    return ({
        ticker: {
            "daily": json_data_hist_daily,
    }})