from fastapi import FastAPI

app = FastAPI(title="GitHub Metrics API")

@app.get("/")
def root():
    return {"message": "API is running!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
