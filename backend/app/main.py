#main.py
from fastapi import FastAPI
from app.routers import auth, users
from app.db.database import Base, engine
from app.models import user  # import your models
from app.db.database import Base, engine
from app.models import user  # import your models

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)





@app.get("/")
def root():
    return {"message": "Welcome to FastAPI JWT App"}


# It must be on bottom


Base.metadata.create_all(bind=engine)

