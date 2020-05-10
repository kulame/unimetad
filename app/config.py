from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "API"
    admin_email: str = "zhengwei@igengmei.com"
    items_per_user: int = 20
    DATABASE_URL:str = "sqlite:///test.db"
    class Config:
        env_file = ".env"


def get_settings():
    settings = Settings()
    return settings

