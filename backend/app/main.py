# main.py 
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine, Base


app = FastAPI()

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers

# Create tables
#Base.metadata.create_all(bind=engine)

@app.get("/")
async def read_root():
    return {"message": "PitchPilot API running"}

# Database models