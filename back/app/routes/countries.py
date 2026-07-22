from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.dependencies import get_db

from app.repositories.country_repository import (
    get_all_countries,
)

router = APIRouter(
    prefix="/countries",
    tags=["Countries"]
)


@router.get("/")
def list_countries(
    db: Session = Depends(get_db)
):
    return get_all_countries(db)