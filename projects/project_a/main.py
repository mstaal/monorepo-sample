import uvicorn
from fastapi import FastAPI
from endpoints.router_a import router as router_a


app = FastAPI()

app.include_router(router_a)
