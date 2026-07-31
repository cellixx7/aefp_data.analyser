from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class Instituicao(Base):
    __tablename__ = "instituicoes"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    sigla: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    nome_extenso: Mapped[str] = mapped_column(
        String(300),
        nullable=False
    )

    pais: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    uf: Mapped[str | None] = mapped_column(
        String(10),
        nullable=True
    )

    continente: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )
