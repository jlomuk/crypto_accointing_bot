from typing import Any, Callable, Optional

from pydantic import BaseModel


class Contex(BaseModel):
    data: Any
    func: Optional[Callable] = None
