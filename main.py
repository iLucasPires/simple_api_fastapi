import uvicorn

from fastapi import FastAPI
from app.database.settings import Base, sqlite_engine
from app.routes.user_route import router_user

with sqlite_engine.begin() as conn:
    Base.metadata.create_all(conn)

app = FastAPI()
app.include_router(router_user)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
