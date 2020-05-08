from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "API"
    admin_email: str = "zhengwei@igengmei.com"
    items_per_user: int = 20

    class Config:
        env_file = ".env"


settings = Settings()
