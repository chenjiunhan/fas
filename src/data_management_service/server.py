import uvicorn
from fastapi import FastAPI, Response
from binance_data_manager import BinanceDataManager
from pydantic import BaseModel

app = FastAPI()
binance_dm = BinanceDataManager()

class KlineData(BaseModel):
    symbol: str
    kline: list

@app.post("/data_manager/binance/kline")
def save_kline(kline_data: KlineData, response: Response):

    result = binance_dm.save_kline_csv(kline_data.symbol, kline_data.kline)

    if result:
        response_json = {
            "success": True,
            "message": "Save binance kline to db success!",
            "status_code": 200
        }
    else:
        response_json = {
            "success": False,
            "message": "Save binance kline to db failed!",
            "status_code": 400
        }
    
    response.status_code = response_json["status_code"]
    return response_json

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', 
                     port=10001, debug=True)