from django.shortcuts import render
import yfinance as yf
from django.http import JsonResponse
from datetime import datetime, timedelta
import json

def to_json_yearly(ticker):
    stock = yf.Ticker(ticker)
    end_date = datetime.today().strftime('%Y-%m-%d')
    start_date = (datetime.today() - timedelta(days=3650)).strftime('%Y-%m-%d')

    hist_yearly = stock.history(start=start_date, end=end_date, interval="3mo")

    json_data_hist_yearly = hist_yearly.to_json(orient='records')

    json_data_hist_yearly = json.loads(json_data_hist_yearly)

    for idx, record in enumerate(json_data_hist_yearly):
        record['date'] = hist_yearly.index[idx]

    return ({
        ticker: {
            "yearly": json_data_hist_yearly,
    }})