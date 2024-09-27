import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from input import CreateEmployee, GetEmployee, DeleteEmployee, UpdateEmployee
from fastAPI.service import Service
from typing import Union

app = FastAPI(docs_url="/docs")

service_instance = Service()


class FastAPI:

    def __init__(self, service: Service):
        self.service = service

    async def fastapi_crud(self, item: Union[CreateEmployee, GetEmployee, DeleteEmployee, UpdateEmployee]):
        try:
            result = self.service.service_call(item)
            return result
        except Exception as err:
            raise HTTPException(status_code=500, detail=str(err))


def get_handler(service: Service = Depends(lambda: service_instance)):
    return FastAPI(service)


@app.post("/create_employee")
async def create_employee(item: CreateEmployee, handler: FastAPI = Depends(get_handler)):
    return await handler.fastapi_crud(item)


@app.get("/get_employee")
async def get_employee(item: GetEmployee, handler: FastAPI = Depends(get_handler)):
    return await handler.fastapi_crud(item)


@app.delete("/delete_employee")
async def delete_employee(item: DeleteEmployee, handler: FastAPI = Depends(get_handler)):
    return await handler.fastapi_crud(item)


@app.put("/update_employee")
async def update_employee(item: UpdateEmployee, handler: FastAPI = Depends(get_handler)):
    return await handler.fastapi_crud(item)


if __name__ == "__main__":
    uvicorn.run(app)
