from fastapi import FastAPI
from app.routers import notification_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configurer CORS
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(notification_router)

@app.get("/")
def read_root():
    return {"message": "Notification Service"}
