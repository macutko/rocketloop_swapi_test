from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import auth, people, films

app = FastAPI()

app.include_router(auth.router)
app.include_router(people.router)
app.include_router(films.router)

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}
