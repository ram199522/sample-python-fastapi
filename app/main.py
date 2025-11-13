from fastapi import FastAPI
from app.routers import hello, test_db  # include both routers

app = FastAPI(title="Sample FastAPI App")

# Include routers
app.include_router(hello.router)
app.include_router(test_db.router)

@app.get("/")
async def root():
    return {"message": "Welcome to Sample FastAPI App!"}
