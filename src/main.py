import os
from pydantic import BaseModel
from dotenv import load_dotenv


class Config(BaseModel):
    api_key: str


def my_func(x: int) -> str:
    return 1

def main():
    load_dotenv()
    config = Config(
        api_key=os.getenv("API_KEY", "no .env file found with API_KEY"),
    )

    print(f"API Key: {config.api_key}")


if __name__ == "__main__":
    main()
