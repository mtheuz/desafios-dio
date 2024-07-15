from typing import Annotated
from pydantic import UUID4, Field
from atletas_api.contrib.schemas import BaseSchema

class CentroTreinamentoIn(BaseSchema):
    nome: Annotated[str, Field(
        description='Nome do centro de treinamento',
        examples=['Centro de Treinamento'],
        max_length=20
    )]
    endereco: Annotated[str, Field(
        description='Endereço do centro de treinamento',
        examples=['Rua 1, 123'],
        max_length=60
    )]
    proprietario: Annotated[str, Field(
        description='Proprietário do centro de treinamento',
        examples=['João'],
        max_length=30
    )]

class CentroTreinamentoOut(CentroTreinamentoIn): 
        id: Annotated[UUID4, Field(description='Identificador do centro de treinamento')]

class CentroTreinamentoAtleta(BaseSchema):
    nome: Annotated[str, Field(
        description='Nome do centro de treinamento',
        examples=['Centro de Treinamento'],
        max_length=20
    )]
