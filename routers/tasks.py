from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder

# user modules
from database.repository import TaskRepository
from schemas.tasks import Task, TaskAdd

router = APIRouter(
    tags = ['task'],
    prefix="/task"
)


@router.post("", response_model=Task)
async def add_task(
        task: Annotated[TaskAdd, Depends()],
    ):
    added_task = await TaskRepository.add(task)
    task_json = jsonable_encoder(added_task)
    return Task(**task_json)


@router.post("/{task_id}")
async def delete_task(task_id: int):
    return await TaskRepository.delete(task_id=task_id)


@router.get("/{task_id}", response_model=Task)
async def get_one_task(task_id: int):
    task = await TaskRepository.get(task_id=task_id)
    task_json = jsonable_encoder(task)
    return Task(**task_json)


@router.get("", response_model=list[Task])
async def get_tasks():
    return await TaskRepository.get_all()


