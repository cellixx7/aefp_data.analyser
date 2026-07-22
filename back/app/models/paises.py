from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class Country(Base):
    __tablename__ = "countries"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True,
    )

    iso3: Mapped[str] = mapped_column(
        String(3),
        nullable=False,
        unique=True,
    )

    continent_id: Mapped[int] = mapped_column(
        ForeignKey("continents.id")
    )

    continent = relationship("Continent")