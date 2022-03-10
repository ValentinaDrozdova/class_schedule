from loguru import logger
from pydantic import BaseSettings, Field
from pathlib import Path


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PORT: int = Field(..., env="PORT")
    DB_NAME: str = Field(..., env="DB_NAME")
    DB_USER: str = Field(..., env="DB_USER")
    DB_PASSWORD: str = Field(..., env="DB_PASSWORD")
    DB_HOST: str = Field(..., env="DB_HOST")
    LOG_FILEPATH: str = Field("logs/app_log.log", env="LOG_FILEPATH")
    ACCESS_TOKEN_DELTA: int = Field(120, env="ACCESS_TOKEN_DELTA")
    SECRET_KEY: str = Field("schedule", env="SECRET_KEY")

    class Config:
        env_file = Path(__file__).parents[1].joinpath(".env")
        logger.info(f"Get envs from {env_file}")
        env_file_encoding = 'utf-8'


settings = Settings()
