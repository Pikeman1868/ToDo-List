from __future__ import annotations
from dataclasses import dataclass
from uuid import UUID, uuid4

@dataclass
class CreateListRequest():
    name : str


@dataclass
class CreateListResponse():
    id : UUID
    name : str


class CreateList():

    def __call__(self, request : CreateListRequest) -> CreateListResponse:
        return CreateListResponse(uuid4(), request.name)