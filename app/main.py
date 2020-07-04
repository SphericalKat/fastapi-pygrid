from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_root():
    return {
        "status": 200,
        "info": "PyGrid with FastApi\nRunning uvicorn 0.11.5 with CPython 3.8.3 on Linux"
    }
