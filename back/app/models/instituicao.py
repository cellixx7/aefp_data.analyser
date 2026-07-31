from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

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
        unique=True,
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
        String(50),
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

    programas: Mapped[list["ProgramaDeFomento"]] = relationship(
        back_populates="instituicao",
    )

    vinculos_como_lider: Mapped[list["BolsistaPesquisador"]] = relationship(
        back_populates="instituicao_lider",
        foreign_keys="BolsistaPesquisador.instituicao_lider_id",
    )

    vinculos_como_solicitante: Mapped[
        list["BolsistaPesquisador"]
    ] = relationship(
        back_populates="instituicao_solicitante",
        foreign_keys="BolsistaPesquisador.instituicao_solicitante_id",
    )
