from typing import Union
import uvicorn
from fastapi import FastAPI
from atletas_api.routers.routers import api_router

app = FastAPI(title="Altletas_API")
app.include_router(api_router)

if __name__ == 'main':
    uvicorn.run('main.app,', host='0.0.0.0', port=8000, log_level='info', reload=True)