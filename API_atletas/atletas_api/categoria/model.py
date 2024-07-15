from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from atletas_api.contrib.model import BaseModel

class CategoriaModel(BaseModel):
    __tablename__ = 'categoria'
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, unique=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    atletas: Mapped['AtletaModel'] = relationship(back_populates='categoria')

