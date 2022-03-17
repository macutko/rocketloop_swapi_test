from fastapi import FastAPI

from routers import auth, people

app = FastAPI()

app.include_router(auth.router)
app.include_router(people.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
