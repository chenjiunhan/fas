import requests
import schedule
import threading
import time
import uvicorn

from reporter import Reporter
from fastapi import FastAPI, Response, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

class Source:

    def __init__(self, name, href, comment):
        self.name = name
        self.href = href
        self.comment = comment

app = FastAPI()
reporter = Reporter()
templates = Jinja2Templates(directory="templates")
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

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

@app.get("/reporter/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):

    sources = []
    sources.append(Source("Crypto Market", "https://coinmarketcap.com/zh-tw/", "Observe crypto market changes"))
    sources.append(Source("DappRadar", "https://dappradar.com/rankings", "Observe Dapp market"))
    sources.append(Source("Opeasea NFT ranking", "https://opensea.io/rankings", "Find investment target"))

    inputs = {
        "request": request, 
        "sources": sources
    }

    return templates.TemplateResponse("dashboard.html", inputs)

@app.get("/reporter/tables", response_class=HTMLResponse)
async def tables(request: Request):
    return templates.TemplateResponse("tables.html", {"request": request})

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