
from fastapi import FastAPI
from app.routers import auth, users

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)


from app.db.database import Base, engine
from app.models import user  # import your models

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI JWT App"}


# It must be on bottom
from app.db.database import Base, engine
from app.models import user  # import your models

Base.metadata.create_all(bind=engine)

