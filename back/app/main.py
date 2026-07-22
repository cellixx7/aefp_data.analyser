from fastapi import FastAPI

from app.db.database import engine
from app.models.base import Base
from app.routes.countries import router as countries_router
from app.models.continent import Continent
from app.models.country import Country

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Portal AEFP API"
)

app.include_router(countries_router)

@app.get("/health")
def health():
    return {
        "status": "online"
    }