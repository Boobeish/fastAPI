import uvicorn
from fastapi import FastAPI
from input import Item


app = FastAPI()


@app.get("/")
def hello_world(item: Item):
    try:
        input_name = item.name
        return {"name": input_name}
    except Exception as err:
        raise err


if __name__ == "__main__":
    uvicorn.run(app)
