from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.routers.webhook import router as webhook_router


origins = [
    "http://localhost:8000",
    "http://localhost:3000",
]

if (settings.debugging):
    app = FastAPI(debug=True, reload=True, port=8001)
else:
    app = FastAPI(port=8001)


@app.get("/health-check", include_in_schema=False)
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(webhook_router)
