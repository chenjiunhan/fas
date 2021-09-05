import os
import pandas as pd

class BinanceDataManager:
    DATA_DIR = os.environ['DATA_DIR']

    def __init__(self):
        pass

    def save_kline_csv(self, symbol, kline):
        columns = [
            "Open time",
            "Open",
            "High",
            "Low",
            "Close",
            "Volume",
            "Close time",
            "Quote asset volume",
            "Number of trades",
            "Taker buy base asset volume",
            "Taker buy quote asset volume",
            "Ignore",
        ]
        file_path = self.symbol_to_csv_path(symbol)
        df = pd.DataFrame(kline, columns=columns)
        df.to_csv(file_path, index=False)
        return os.path.exists(file_path)

    def symbol_to_csv_path(self, symbol):
        file_name = f"{symbol}.csv"
        file_path = os.path.join(self.DATA_DIR, file_name)
        return file_path
