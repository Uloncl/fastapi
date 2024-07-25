from fastapi import FastAPI
import httpx
import asyncio

app = FastAPI()

@app.get("/")
async def root():
    response = await httpx.AsyncClient().get("https://neocities.org/api/info?sitename=uloncl")
    return response.text