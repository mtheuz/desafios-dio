from pydantic import UUID4
from sqlalchemy.future import select
from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException,status
from atletas_api.categoria.model import CategoriaModel
from atletas_api.categoria.schemas import CategoriaIn, CategoriaOut
from atletas_api.contrib.dependencies import DatabaseSession

router = APIRouter()

@router.post('/',
             summary='Create a new categoria',
             status_code=status.HTTP_201_CREATED,
             response_model=CategoriaOut
             )

async def post(db_session: DatabaseSession, categoria_in: CategoriaIn = Body(...))->CategoriaOut:
    categoria_out = CategoriaOut(id=uuid4(), **categoria_in.model_dump())
    categoria_model = CategoriaModel(**categoria_out.model_dump())
    db_session.add(categoria_model)
    await db_session.commit()
    #breakpoint()
    return categoria_out

@router.get('/',
             summary='Get all categorias',
             status_code=status.HTTP_200_OK,
             response_model=list[CategoriaOut]
             )

async def query(db_session: DatabaseSession)->list[CategoriaOut]:
    categorias: list[CategoriaOut] = (await db_session.execute(select(CategoriaModel))).scalars().all()
    #breakpoint()
    return categorias
@router.get('/(id)',
             summary='Get all categorias',
             status_code=status.HTTP_200_OK,
             response_model=CategoriaOut
             )

async def query(id:UUID4,db_session: DatabaseSession)->CategoriaOut:
    categoria: list[CategoriaOut] = (await db_session.execute(select(CategoriaModel).filter_by(id=id))).scalars().first()
    #breakpoint()
    if not categoria:
        raise HTTPException(status_code=404, detail='Categoria not found')
    return categoria