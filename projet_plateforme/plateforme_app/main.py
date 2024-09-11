from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from datetime import timedelta, datetime
from fastapi.middleware.cors import CORSMiddleware

# Import des fichiers locaux (auth, schemas, models, routers)
from projet_plateforme.plateforme_app.auth import create_access_token, verify_password, get_password_hash
from projet_plateforme.plateforme_app.schemas import Token, TokenData, UserInDB
from projet_plateforme.plateforme_app.database import engine, SessionLocal
from projet_plateforme.plateforme_app.models import student_model, admin_model, forum_user_model, subject_model, profile_model, discussion_model, message_model
from projet_plateforme.plateforme_app.routers import students, admins, forum_users, subjects, profiles, discussions, messages


# Configuration des modèles (tables) dans la base de données
student_model.Base.metadata.create_all(bind=engine)
admin_model.Base.metadata.create_all(bind=engine)
forum_user_model.Base.metadata.create_all(bind=engine)
subject_model.Base.metadata.create_all(bind=engine)
profile_model.Base.metadata.create_all(bind=engine)
discussion_model.Base.metadata.create_all(bind=engine)
message_model.Base.metadata.create_all(bind=engine)


# Création de l'application FastAPI
app = FastAPI()

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

# Schéma OAuth2 pour l'authentification
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Fake database pour l'exemple d'authentification
fake_users_db = {
    "alphandiaye": {
        "username": "alphandiaye_",
        "full_name": "Alpha Ndiaye",
        "email": "alphandiayee@example.com",
        "hashed_password": get_password_hash("secret"),
        "disabled": False,
    }
}

# Algorithme et clé secrète pour les JWT
SECRET_KEY = "DIT_PROJECT1"  # À remplacer par une clé plus sécurisée
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Fonction pour récupérer l'utilisateur depuis la "fake database"
def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

# Fonction pour authentifier l'utilisateur
def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

# Création d'un access token
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# Récupérer les informations de l'utilisateur connecté
@app.get("/users/me", response_model=UserInDB)
async def read_users_me(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

# Fonction pour obtenir la base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Inclusion des routeurs CRUD pour la plateforme
app.include_router(students.router)
app.include_router(admins.router)
app.include_router(forum_users.router)
app.include_router(subjects.router)
app.include_router(profiles.router)
app.include_router(discussions.router)
app.include_router(messages.router)

# Route simple pour vérifier que l'API fonctionne
@app.get("/")
def read_root():
    return {"message": "Bienvenue sur la plateforme DIT !"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
