from enum import Enum

from pydantic import BaseSettings
from dotenv import load_dotenv


class EnvironmentType(str, Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    TEST = "test"


class BaseConfig(BaseSettings):
    class Config:
        case_sensitive = False


class Config(BaseConfig):
    DEBUG: int = 0
    DEFAULT_LOCALE: str = "en_US"
    ENVIRONMENT: str = EnvironmentType.DEVELOPMENT
    RELEASE_VERSION: str = "0.1"
    SECRET_KEY: str = "super-secret-key"
    OMDB_APIKEY: str


load_dotenv()
config: Config = Config()
