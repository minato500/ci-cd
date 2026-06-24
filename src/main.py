from fastapi import FastAPI

app = FastAPI(title="Secure CI/CD App")

@app.get("/")
def read_root():
    return {"status": "healthy", "message": "Application is running cleanly."}

@app.get("/api/v1/data")
def read_secure_data():
    return {"data": "Secure pipeline deployment complete."}
