from fastapi import APIRouter
from atletas_api.atletas.controller import router as atletas_router
from atletas_api.categoria.controller import router as categoria_router
from atletas_api.centro_treinamento.controller import router as centro_treinamento_controller

api_router = APIRouter()

api_router.include_router(atletas_router, prefix='/atletas', tags=['Atletas'])
api_router.include_router(categoria_router, prefix='/categorias', tags=['Categoria'])
api_router.include_router(centro_treinamento_controller, prefix='/ct', tags=['Centro de Treinamento'])