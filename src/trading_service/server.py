import requests
import schedule
import threading
import time
import uvicorn

from trader import Trader
from fastapi import FastAPI, Response
from pydantic import BaseModel

app = FastAPI()
trader = Trader()

@app.get("/trader/heart_beat")
def heart_beat(response: Response):
    response_json = {
        "success": True,
        "message": "Trader is alive!",
        "status_code": 200,
    }
    
    response.status_code = response_json["status_code"]
    return response_json

def cron():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    t = threading.Thread(target = cron)
    t.daemon = True
    t.start()

    uvicorn.run(app, host='0.0.0.0', 
                     port=10005, debug=True)