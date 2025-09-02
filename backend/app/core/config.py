from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    LITELLM_MODEL: str = "openai/gpt-4o"
    
    class Config:
        env_file = ".env"

settings = Settings()