from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/")
async def root():
    response = await client.get("https://neocities.org/api/info?sitename=uloncl")
    return response.text