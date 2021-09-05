import uvicorn
from fastapi import FastAPI, Response
from binance_data_miner import BinanceDataMiner
from pydantic import BaseModel

app = FastAPI()
binance_dmi = BinanceDataMiner()

class MineKlineInput(BaseModel):
    symbol: str

@app.post("/data_miner/binance/kline")
def mine_kline(mine_kline_input: MineKlineInput, response: Response):
    kline = binance_dmi.get_kline_from_db(mine_kline_input.symbol)
    if not kline:
        response_json = {
            "success": False,
            "message": "Get binance kline from db failed!",
            "status_code": 400
        }

        response.status_code = response_json["status_code"]
        return response_json

    filename = "mined_" + mine_kline_input.symbol + ".csv"
    mined_kline_data = binance_dmi.mine_kline_csv(kline)
    save_db_result = binance_dmi.save_mined_kline_data_to_db(filename, mined_kline_data)
    
    if save_db_result:
        response_json = {
            "success": True,
            "message": "Mine binance kline success!",
            "status_code": 200,
            "result": mined_kline_data
        }
    else:
        response_json = {
            "success": False,
            "message": "Save binance mined kline data to db failed!",
            "status_code": 400
        }
    
    response.status_code = response_json["status_code"]
    return response_json

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', 
                     port=10002, debug=True)