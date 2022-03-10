from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from uvicorn import run

from db import init_db
from logger import setup_logger
from settings.settings import settings
from routers import v1_api

app = FastAPI(title="ClassSchedule")
app.include_router(v1_api, prefix=settings.API_V1_STR)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    setup_logger()
    await init_db()

    #  FIXME HARDCODE DEFAULT USER

def main():
    run(app, port=settings.PORT)


if __name__ == '__main__':
    main()
