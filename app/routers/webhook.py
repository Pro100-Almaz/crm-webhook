from fastapi import status, HTTPException, Depends, APIRouter, Request
from fastapi.responses import RedirectResponse

from typing import List

import app.schemas as schemas
from app.helpers.database import database
from app.config import settings

import requests


router = APIRouter(
    prefix = "/webhook",
    tags = ['webhook']
)


@router.post("/tg")
async def get_message(update: Request):
    data = await update.json()

    chat_id = data.get("message", {}).get("chat", {}).get("id")
    text = data.get("message", {}).get("text")

    print(data)
    # Handle the Telegram update (e.g., sending a response)
    return {"status": "ok"}


@router.post(f"/webhook")
async def telegram_webhook(update: Request):
    data = await update.json()
    chat_id = data.get("message", {}).get("chat", {}).get("id")
    text = data.get("message", {}).get("text")

    if chat_id and text:
        # Send a response message
        await send_message(chat_id, f"You said: {text}")

    return {"status": "ok"}


async def send_message(chat_id: int, text: str):
    import httpx
    async with httpx.AsyncClient() as client:
        url = f"https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage"
        payload = {"chat_id": chat_id, "text": text}
        await client.post(url, json=payload)