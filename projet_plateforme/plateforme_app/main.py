from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import engine, SessionLocal
from models import student_model, admin_model, forum_user_model, subject_model, profile_model, discussion_model, message_model
from routers import students, admins, forum_users, subjects, profiles, discussions, messages


student_model.Base.metadata.create_all(bind=engine)
admin_model.Base.metadata.create_all(bind=engine)
forum_user_model.Base.metadata.create_all(bind=engine)
subject_model.Base.metadata.create_all(bind=engine)
profile_model.Base.metadata.create_all(bind=engine)
discussion_model.Base.metadata.create_all(bind=engine)
message_model.Base.metadata.create_all(bind=engine)


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app.include_router(students.routers)
app.include_router(admins.routers)
app.include_router(forum_users.routers)
app.include_router(subjects.routers)
app.include_router(profiles.routers)
app.include_router(discussions.routers)
app.include_router(messages.routers)


@app.get("/")
def read_root():
    return {"message": "Bienvenue sur la plateforme DIT !"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
