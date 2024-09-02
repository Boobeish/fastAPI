import uvicorn
from fastapi import FastAPI, HTTPException

from fastAPI import service
from input import Employee
from fastAPI.service import Service

app = FastAPI()

service_instance = Service()
# class API:
# 
#     def __init__(self, service=None):
#         # self.app = FastAPI()
#         # self.app = None
#         self.service = service or Service()
#         # self.setup_routes()
#
#     # def setup_routes(self):
@app.post("/")
def fastapi_crud(item: Employee):
    try:
        result = service_instance.service_call(item, 'C')
            # result = dbl.db_activity(self, employee, 'C')
        return result
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
