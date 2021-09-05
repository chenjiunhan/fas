import requests
import schedule
import threading
import time
import uvicorn

from binance_data_collector import BinanceDataCollector
from fastapi import FastAPI, Response
from pydantic import BaseModel


app = FastAPI()
binance_dc = BinanceDataCollector()

class CollectKlineInput(BaseModel):
    symbol: str

@app.post("/data_collector/binance/kline")
async def collect_kline(collect_kline_input: CollectKlineInput, response: Response):
    kline = binance_dc.collect_kline(collect_kline_input.symbol)

    if kline:
        if binance_dc.save_kline_to_db(collect_kline_input.symbol, kline):
            response_json = {
                "success": True,
                "message": "Save binance kline success!",
                "status_code": 200
            }
        else:
            response_json = {
                "success": False,
                "message": "Save to db failed!",
                "status_code": 400
            }
    else:
        response_json = {
            "success": False,
            "message": "Get binance kline failed!",
            "status_code": 400
        }

    response.status_code = response_json["status_code"]
    return response_json

def cron():
    schedule.every().day.at("00:00").do(request_collect_kline, symbol="BTCUSDT")
    schedule.every().day.at("00:00").do(request_collect_kline, symbol="DOGEUSDT")
    schedule.every().day.at("00:00").do(request_collect_kline, symbol="ETHBTC")

    while True:
        schedule.run_pending()
        time.sleep(1)

def request_collect_kline(symbol):
    data = {
        "symbol": symbol
    }
    
    r = requests.post("http://data_collector:10000/data_collector/binance/kline", json=data)

    if r.status_code == 200:
        return r.json()
    else:
        return False

if __name__ == "__main__":

    t = threading.Thread(target = cron)
    t.daemon = True
    t.start()

    uvicorn.run(app, host='0.0.0.0', 
                     port=10000, debug=True)

