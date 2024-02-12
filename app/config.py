from starlette.config import Config

config = Config(".env")


DEBUG: bool = config("DEBUG", cast=bool, default=False)
TESTING: bool = config("TESTING", cast=bool, default=False)

API_PREFIX: str = config("API_PREFIX", default="")
API_HOST: str = config("API_HOST", default="0.0.0.0")
API_PORT: int = config("API_PORT", cast=int, default=8000)

DB_URL: str = config("TEST_DB_URL" if TESTING else "DB_URL")
REPLACE_IF_EXIST: bool = config("REPLACE_IF_EXIST", default=False)
