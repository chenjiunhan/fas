import requests

class BinanceDataCollector:
    
    def BinanceDataCollector(self):
        pass

    @staticmethod
    def collect_kline(symbol): #e.g. BTCUSDT
        params = {
            "symbol": symbol,
            "interval": "1d",
            "limit": 1000,
        }
        r = requests.get("https://api.binance.com/api/v3/klines", params=params)
        
        if r.status_code == 200:
            return r.json()
        else:
            return False

    @staticmethod
    def save_kline_to_db(symbol, kline):
        data = {
            "symbol": symbol,
            "kline": kline
        }
        
        r = requests.post("http://data_manager:10001/data_manager/binance/kline", json=data)

        if r.status_code == 200:
            return r.json()
        else:
            return False

    def run(self):
        pass

    def add_schedule(self, **params):
        pass