from fastapi import status, HTTPException, Depends, APIRouter, Request
from fastapi.responses import RedirectResponse

from sqlalchemy.orm import Session
from typing import List

import app. as schemas
import src.models as models
from src.helpers.database import get_db
from src.helpers.utils import hash, verify
from src.config import settings

import requests


router = APIRouter(
    prefix = "/webhook",
    tags = ['webhook']
)


@router.get("/tg")
def get_message(data, db: Session = Depends(get_db)):
    print(data)