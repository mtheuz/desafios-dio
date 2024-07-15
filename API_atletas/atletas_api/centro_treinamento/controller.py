from pydantic import UUID4
from sqlalchemy.future import select
from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException,status
from atletas_api.centro_treinamento.model import CentroTreinamentoModel
from atletas_api.centro_treinamento.schemas import CentroTreinamentoModelIn, CentroTreinamentoModelOut
from atletas_api.contrib.dependencies import DatabaseSession

router = APIRouter()

@router.post('/',
             summary='Create a new ',
             status_code=status.HTTP_201_CREATED,
             response_model=CentroTreinamentoModelOut
             )

async def post(db_session: DatabaseSession, categoria_in: CentroTreinamentoModelIn = Body(...))->CentroTreinamentoModelOut:
    categoria_out = CentroTreinamentoModelOut(id=uuid4(), **categoria_in.model_dump())
    centro_treinamento_model = CentroTreinamentoModel(**categoria_out.model_dump())
    db_session.add(centro_treinamento_model)
    await db_session.commit()
    #breakpoint()
    return categoria_out

@router.get('/',
             summary='Get all categorias',
             status_code=status.HTTP_200_OK,
             response_model=list[CentroTreinamentoModelOut]
             )

async def query(db_session: DatabaseSession)->list[CentroTreinamentoModelOut]:
    categorias: list[CentroTreinamentoModelOut] = (await db_session.execute(select(CentroTreinamentoModel))).scalars().all()
    #breakpoint()
    return categorias
@router.get('/(id)',
             summary='Get all categorias',
             status_code=status.HTTP_200_OK,
             response_model=CentroTreinamentoModelOut
             )

async def query(id:UUID4,db_session: DatabaseSession)->CentroTreinamentoModelOut:
    categoria: list[CentroTreinamentoModelOut] = (await db_session.execute(select(CentroTreinamentoModel).filter_by(id=id))).scalars().first()
    #breakpoint()
    if not categoria:
        raise HTTPException(status_code=404, detail='Categoria not found')
    return categoria