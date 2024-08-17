from fastapi import FastAPI
import uvicorn

app= FastAPI()

@app.get("/")
async def rout():
    return "welcom to order service"


def start():
    uvicorn.run("app.main:app", host="0.0.0.0", port=8002, reload=True)