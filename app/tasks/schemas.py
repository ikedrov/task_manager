from pydantic import BaseModel


class STasks(BaseModel):
    id: int
    title: str
    description: str
    completed: bool
    owner_id: int

    class Config:
        from_attributes = True



