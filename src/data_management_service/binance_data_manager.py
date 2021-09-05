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
        filename = f"{symbol}.csv"
        file_path = os.path.join(self.DATA_DIR, filename)
        return file_path

    def get_kline_csv(self, symbol):
        file_path = self.symbol_to_csv_path(symbol)
        if os.path.exists(file_path):
            with open(file_path, "r") as f_csv:
                csv_content = f_csv.read()
            return csv_content
        else:
            return False

    def save_mined_kline_data_csv(self, filename, mined_kline_data):
        file_path = os.path.join(self.DATA_DIR, filename)
        with open(file_path, 'w') as f:
            f.write(mined_kline_data)
        return True

