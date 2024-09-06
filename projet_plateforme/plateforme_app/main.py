from fastapi import FastAPI
from .projet_plateforme.plateforme_app.routes import students, admin, forumUser, sujets, profiles, discussion, message
from .projet_plateforme.plateforme_app.database import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(students.routes)
app.include_router(admin.routes)
app.include_router(forumUser.routes)
app.include_router(sujets.routes)
app.include_router(profiles.routes)
app.include_router(discussion.routes)
app.include_router(message.routes)