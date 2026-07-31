from fastapi import FastAPI

app = FastAPI(
    title="Portal AEFP API",
    description="API institucional do Portal AEFP",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "application": "Portal AEFP API",
        "documentation": "/docs",
    }


@app.get("/health", tags=["Monitoramento"])
def health_check():
    return {
        "status": "ok",
        "application": "Portal AEFP",
    }