from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from atletas_api.configs.database import get_session

DatabaseSession = Annotated[AsyncSession, Depends(get_session)]