from todolist.createlist import CreateList, CreateListRequest, CreateListResponse
from uuid import UUID

_CREATE_LIST = CreateList()


def create_list(name:str) -> UUID:
    request = CreateListRequest(name)
    resp = _CREATE_LIST(request=request)
    return resp.id