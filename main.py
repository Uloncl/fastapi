from fastapi import FastAPI
import httpx
import asyncio

app = FastAPI()

@app.get("/")
async def root():
    response = await httpx.get("https://neocities.org/api/info?sitename=uloncl")
    return response.json()