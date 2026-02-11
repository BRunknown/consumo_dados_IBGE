from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encondig="utf-8")

    LOG_LEVEL: str
    CONSOLE_LOG: bool
    TIMEOUT_SEC: float
    RESPONSE_SAVE_PATH: str
    
