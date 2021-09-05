import requests

class BinanceDataMiner:
    
    def BinanceDataMiner(self):
        pass

    @staticmethod
    def get_kline_from_db(symbol): #e.g. BTCUSDT
        params = {
            "symbol": symbol
        }
        r = requests.get("http://data_manager:10001/data_manager/binance/kline", params=params)
        
        if r.status_code == 200:
            return r.json()["result"]
        else:
            return False

    @staticmethod
    def mine_kline_csv(kline):
        mined_kline_data = kline
        return mined_kline_data

    @staticmethod
    def save_mined_kline_data_to_db(filename, mined_kline_data):
        data = {
            "filename": filename,
            "mined_kline_data": mined_kline_data
        }
        
        r = requests.post("http://data_manager:10001/data_manager/binance/mined_kline_data", json=data)

        if r.status_code == 200:
            return r.json()
        else:
            return False