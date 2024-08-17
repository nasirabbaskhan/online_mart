from fastapi import FastAPI
import uvicorn

app= FastAPI()

@app.get("/")
async def rout():
    return "Welcoe to our user Service"



def start():
    uvicorn.run("app.main:app", host= "0.0.0.0", port= 8005, reload=True)