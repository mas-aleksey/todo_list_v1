from pydantic import BaseModel, UUID4


class TodoListResponse(BaseModel):
    id: UUID4
    title: str


class TodoListRequest(BaseModel):
    title: str
