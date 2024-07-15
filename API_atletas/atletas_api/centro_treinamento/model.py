
from sqlalchemy import Integer, String
from atletas_api.contrib.model import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship


class CentroTreinamentoModel(BaseModel):
    __tablename__ = 'centro_treinamento'
    pk_id: Mapped[int] =  mapped_column(Integer, primary_key=True, autoincrement=True, unique=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    endereco: Mapped[str] = mapped_column(String(60), nullable=False)
    proprietario: Mapped[str] = mapped_column(String(30), nullable=False)
    atletas: Mapped['AtletaModel'] = relationship(back_populates='centro_treinamento')



    