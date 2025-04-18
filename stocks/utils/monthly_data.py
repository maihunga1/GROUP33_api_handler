from django.shortcuts import render
import yfinance as yf
from django.http import JsonResponse
from datetime import datetime, timedelta
import json

def to_json_monthly(ticker):
    stock = yf.Ticker(ticker)
    end_date = datetime.today().strftime('%Y-%m-%d')
    start_date = (datetime.today() - timedelta(days=730)).strftime('%Y-%m-%d')

    hist_monthly = stock.history(start=start_date, end=end_date, interval="1mo")

    json_data_hist_monthly = hist_monthly.to_json(orient='records')

    json_data_hist_monthly = json.loads(json_data_hist_monthly)

    for idx, record in enumerate(json_data_hist_monthly):
        record['date'] = hist_monthly.index[idx]

    return ({
        ticker: {
            "monthly": json_data_hist_monthly,
    }})