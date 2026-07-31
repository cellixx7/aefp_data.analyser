from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import Date, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

if TYPE_CHECKING:
    from app.models.bolsistas_pesquisadores import BolsistaPesquisador
    from app.models.instituicao import Instituicao


class ProgramaDeFomento(Base):
    __tablename__ = "programas_fomento"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    # Identificador original da aba PROGRAMAS DE FOMENTO.
    id_fonte: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        unique=True,
        index=True,
    )

    # Instituição informada na coluna SIGLA IES.
    instituicao_id: Mapped[int | None] = mapped_column(
        ForeignKey("instituicoes.id"),
        nullable=True,
        index=True,
    )

    numero_processo_concessao: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    numero_proposta: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    nome: Mapped[str] = mapped_column(
        String(300),
        nullable=False,
        index=True,
    )

    titulo_pesquisa: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    resumo: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    eixo_tematico_oficial: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True,
    )

    eixo_tematico_aefp: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True,
    )

    dominio: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True,
    )

    dominio_secundario: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True,
    )

    quantidade_bolsas: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    status: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
        index=True,
    )

    data_inicio: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    data_termino: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    fonte: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True,
    )

    instituicao: Mapped["Instituicao | None"] = relationship(
        back_populates="programas",
    )

    vinculos_bolsistas: Mapped[list["BolsistaPesquisador"]] = relationship(
        back_populates="programa",
    )
