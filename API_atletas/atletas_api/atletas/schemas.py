from typing import Annotated
from pydantic import Field, PositiveFloat
from atletas_api.contrib.schemas import BaseSchema

class Atletas(BaseSchema):
    nome: Annotated[str, Field(
        description='Nome do atleta',
        examples=['Matheus'],
        max_length=50
    )]
    cpf: Annotated[str, Field(
        description='CPF do atleta',
        examples=['123.456.789-00'],
        max_length=14
    )]
    idade: Annotated[int, Field(
        description='Idade do atleta',
        examples=[20]
    )]
    peso: Annotated[PositiveFloat, Field(
        description='Peso do atleta',
        examples=[70.5]
    )]
    altura: Annotated[PositiveFloat, Field(
        description='Altura do atleta',
        examples=[1.75]
    )]
    sexo: Annotated[str, Field(
        description='Sexo do atleta',
        examples=['M'],
        max_length=1
    )]

class AtletasIn(Atletas):
    pass
    
class AtletasOut(Atletas):
    pass
