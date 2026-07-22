from sqlalchemy.orm import Session

from app.models.country import Country


def get_all_countries(db: Session):
    return db.query(Country).all()