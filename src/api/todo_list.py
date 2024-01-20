from fastapi import APIRouter, Depends
from src.controller.todo import get_todo_controller, TodoController
from src.schemas.todo import TodoListResponse, TodoListRequest
from pydantic import UUID4

router = APIRouter()


@router.get(
    "/lists",
    response_model=list[TodoListResponse]
)
async def get_lists(
    todo_controller: TodoController = Depends(get_todo_controller),
) -> list[TodoListResponse]:
    result = await todo_controller.get_lists()
    return result


@router.post(
    "/lists",
    response_model=TodoListResponse,
    status_code=201,
)
async def create_list(
    todo_request: TodoListRequest,
    todo_controller: TodoController = Depends(get_todo_controller),
) -> TodoListResponse:
    result = await todo_controller.create_lists(todo_request.title)
    return result


@router.delete(
    "/lists/{list_id}",
    status_code=204,
)
async def delete_list(
    list_id: UUID4,
    todo_controller: TodoController = Depends(get_todo_controller),
):
    await todo_controller.delete_list(list_id)
