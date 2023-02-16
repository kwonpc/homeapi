import uvicorn
from fastapi import FastAPI
from api import property, info, apply, regHome

app = FastAPI()
app.include_router(property.router)
app.include_router(info.router)
app.include_router(apply.router)
app.include_router(regHome.router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
