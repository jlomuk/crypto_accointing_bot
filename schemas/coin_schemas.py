from pydantic import BaseModel, validator


class Coin(BaseModel):
    id: int
    shortcut: str
    name: str
    capitalization: int | None


class DeleteCoinRequest(BaseModel):
    shortcut: str

    @validator('shortcut')
    def upper_shortcut(cls, v: str):
        return v.upper()


class CreateCoinRequest(DeleteCoinRequest):
    shortcut: str
    name: str


class GetCoinRequest(DeleteCoinRequest):
    shortcut: str

    @validator('shortcut', pre=True)
    def split_str(cls, v):
        if not isinstance(v, str) and not v.startswith('/get_coin'):
            raise ValueError
        s = v.split('/get_coin')
        if len(s) == 2:
            return s[1]
