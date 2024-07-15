from typing import Annotated
from pydantic import UUID4, Field
from atletas_api.contrib.schemas import BaseSchema

class CategoriaIn(BaseSchema):
    nome: Annotated[str, Field(
        description='Nome do atleta',
        examples=['Matheus'],  # Corrected to a list of examples
        max_length=10  # Corrected: max_length should be an integer
    )]
    
class CategoriaOut(CategoriaIn):
    id: Annotated[UUID4, Field(description='Identificador da categoria')]

    # You can add more fields specific to CategoriaOut here
