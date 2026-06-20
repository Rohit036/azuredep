from fastapi import FastAPI
import os
from datetime import datetime

app = FastAPI(title="Azure Demo API", version="1.0.0")

@app.get("/")
def read_root():
    return {
        "message": "Hello from Azure Container Apps!",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "environment": os.getenv("ENVIRONMENT", "development")
    }

@app.get("/config")
def get_config():
    # Demonstrate reading secrets from Key Vault (via environment variables)
    return {
        "database_configured": bool(os.getenv("DATABASE_URL")),
        "api_key_configured": bool(os.getenv("API_KEY")),
        "environment": os.getenv("ENVIRONMENT", "development")
    }