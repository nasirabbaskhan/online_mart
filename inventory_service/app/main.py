from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def rout():
    return "Welcome to Inventory service"



def start():
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)