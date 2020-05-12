from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "API"
    admin_email: str = "zhengwei@igengmei.com"
    items_per_user: int = 20
    DATABASE_URL:str ="mysql://root:111111@127.0.0.1:3306/unimetad"


def get_settings():
    settings = Settings()
    return settings

