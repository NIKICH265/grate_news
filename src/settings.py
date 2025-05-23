from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    SECRET_KEY: str
    ALGORITHM: str
    DATABASE_PATH: str
    DEBUG: bool
    NEWS_STATUS: dict = {"confirm": "confirm", "pending": "pending", "reject": "reject"}

    @property
    def db_path(self):
        return f"sqlite:///{self.DATABASE_PATH}"


settings = Settings()
