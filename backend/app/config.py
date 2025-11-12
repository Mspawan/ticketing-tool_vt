import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # PostgreSQL database connection
    # It will first check for DATABASE_URL in environment variables (Azure),
    # and if not found, use the fallback value for local testing.
    database_url: str = os.getenv(
        "DATABASE_URL",
        "postgresql+asyncpg://pawanadmin:Azure%4012345@ticketingdbserver.postgres.database.azure.com:5432/postgres"
    )
    
    backend_host: str = "0.0.0.0"
    backend_port: int = 8000
    allowed_origins: list = ["http://localhost:3000", "http://localhost:3001", "http://127.0.0.1:3001"]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"

settings = Settings()
