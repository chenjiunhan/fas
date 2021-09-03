import uvicorn
from fastapi import FastAPI
from binance_data_collector import BinanceDataCollector
from pydantic import BaseModel

class Pairs(BaseModel):
    symbol_1: str
    symbol_2: str

app = FastAPI()
binance_dc = BinanceDataCollector()

@app.post("/data_collector/binance/pair_csv")
def collect_pair(pairs: Pairs):
    return binance_dc.collect_pair(pairs.symbol_1, pairs.symbol_2)

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', 
                     port=10000, debug=True)