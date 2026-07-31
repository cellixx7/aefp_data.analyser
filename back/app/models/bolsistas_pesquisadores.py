from datetime import date
from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import Date, ForeignKey, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

if TYPE_CHECKING:
    from app.models.instituicao import Instituicao
    from app.models.programas_de_fomento import ProgramaDeFomento


class BolsistaPesquisador(Base):
    __tablename__ = "bolsistas_pesquisadores"

    # Chave interna de cada linha ou vínculo da planilha.
    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    # Valor original da coluna ID RELAÇÕES.
    # Pode repetir porque vários bolsistas pertencem ao mesmo programa.
    id_relacoes_fonte: Mapped[int] = mapped_column(
        nullable=False,
        index=True,
    )

    # Programa relacionado pelo ID RELAÇÕES.
    programa_id: Mapped[int | None] = mapped_column(
        ForeignKey("programas_fomento.id"),
        nullable=True,
        index=True,
    )

    # Instituição da coluna IES Lider.
    instituicao_lider_id: Mapped[int | None] = mapped_column(
        ForeignKey("instituicoes.id"),
        nullable=True,
        index=True,
    )

    # Instituição da coluna IES/OM.
    instituicao_solicitante_id: Mapped[int | None] = mapped_column(
        ForeignKey("instituicoes.id"),
        nullable=True,
        index=True,
    )

    # Texto original da coluna Programas de Fomento.
    programa_fonte: Mapped[str | None] = mapped_column(
        String(300),
        nullable=True,
    )

    nome: Mapped[str] = mapped_column(
        String(300),
        nullable=False,
        index=True,
    )

    classificacao: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    eixo_tematico: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True,
    )

    modalidade: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
        index=True,
    )

    data_inicio: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    data_finalizacao: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    conclusao: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    situacao: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
        index=True,
    )

    observacoes: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    pagamento_bolsa: Mapped[Decimal | None] = mapped_column(
        Numeric(14, 2),
        nullable=True,
    )

    ultimo_pagamento: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    programa: Mapped["ProgramaDeFomento | None"] = relationship(
        back_populates="vinculos_bolsistas",
    )

    instituicao_lider: Mapped["Instituicao | None"] = relationship(
        back_populates="vinculos_como_lider",
        foreign_keys=[instituicao_lider_id],
    )

    instituicao_solicitante: Mapped["Instituicao | None"] = relationship(
        back_populates="vinculos_como_solicitante",
        foreign_keys=[instituicao_solicitante_id],
    )
