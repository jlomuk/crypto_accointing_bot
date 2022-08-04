from typing import Any, Callable

from pydantic import BaseModel


class Contex(BaseModel):
    data: Any
    func: Callable | None
