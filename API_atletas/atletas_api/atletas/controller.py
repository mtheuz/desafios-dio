from fastapi import APIRouter, Body,status

from atletas_api.atletas.schemas import AtletasIn
from atletas_api.contrib.dependencies import DatabaseSession

router = APIRouter()

@router.post('/',
             summary='Create a new atleta',
             status_code=status.HTTP_201_CREATED,)

async def post(db_session: DatabaseSession, atleta: AtletasIn = Body(...)):
    
    pass