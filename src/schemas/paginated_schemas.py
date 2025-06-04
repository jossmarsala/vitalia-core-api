from typing import Optional
from pydantic import BaseModel

class PaginationMeta(BaseModel):
    items_per_page: int
    next_cursor: Optional[str] = None
    has_next_page: bool

    