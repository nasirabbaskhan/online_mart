from fastapi import FastAPI
import uvicorn

app= FastAPI()

@app.get("/")
async def rout():
    return "Welcome to our payment Service"


def start():
    uvicorn.run("app.main:app", host="0.0.0.0", port=8003, reload=True)