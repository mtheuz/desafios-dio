from datetime import datetime
from sqlalchemy import Integer, String, Float, DateTime, ForeignKey
from atletas_api.contrib.model import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship

class AtletaModel(BaseModel):
    __tablename__ = 'atletas'
    pk_id: Mapped[int] =  mapped_column(Integer, primary_key=True, autoincrement=True, unique=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(14), unique=True,  nullable=False)
    idade: Mapped[int] = mapped_column(Float, nullable=False)
    peso: Mapped[float] = mapped_column(Float, nullable=False)
    altura: Mapped[float] = mapped_column(Float, nullable=False)
    sexo: Mapped[str] = mapped_column(String(1), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now)
    categoria: Mapped['CategoriaModel'] = relationship(back_populates='atletas')
    categoria_id: Mapped[int] = mapped_column(Integer, ForeignKey('categoria.pk_id'), unique=True)
    centro_treinamento: Mapped['CentroTreinamentoModel'] = relationship(back_populates='atletas')
    centro_treinamentoid: Mapped[int] = mapped_column(Integer, ForeignKey('centro_treinamento.pk_id'), unique=True)

    