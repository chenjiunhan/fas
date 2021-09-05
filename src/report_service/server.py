import requests
import schedule
import threading
import time
import uvicorn

from reporter import Reporter
from fastapi import FastAPI, Response
from pydantic import BaseModel

app = FastAPI()
reporter = Reporter()

@app.get("/reporter/report")
def report(response: Response):
    report_content = "this is a report."

    response_json = {
        "success": True,
        "message": "Report!",
        "status_code": 200,
        "result": report_content
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
                     port=10004, debug=True)