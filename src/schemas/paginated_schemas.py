from pydantic import BaseModel

class PaginationMeta(BaseModel):
    current_page: int
    total_pages: int
    total_items: int
    items_per_page: int
    has_previous: bool
    has_next: bool

    