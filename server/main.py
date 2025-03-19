from fastapi import FastAPI
from controllers import routers

app = FastAPI()

for router in routers:
    app.include_router(router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
