from pydantic import BaseModel


class Coin(BaseModel):
    id: int
    shortcut: str
    name: str
    capitalization: int | None



