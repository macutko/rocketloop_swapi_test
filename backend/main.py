from fastapi import FastAPI

from routers import auth, people, films

app = FastAPI()

app.include_router(auth.router)
app.include_router(people.router)
app.include_router(films.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
