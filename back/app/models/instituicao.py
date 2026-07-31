from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class Instituicao(Base):
    __tablename__ = "instituicoes"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    sigla: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        index=True,
    )

    nome_extenso: Mapped[str] = mapped_column(
        String(300),
        nullable=False,
        index=True,
    )

    pais: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    uf: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
    )

    tipo_ies: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    continente: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        index=True,
    )
