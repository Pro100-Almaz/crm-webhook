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


@router.get("/tg")
def get_message(data):
    print(data)