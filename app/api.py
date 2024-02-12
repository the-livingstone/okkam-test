from fastapi import APIRouter, Depends

from app.schemas import GetPercentSchema
from app.service import DataService

router = APIRouter()


@router.get("/getPercent", response_model=GetPercentSchema)
async def get_percent(
    audience1: str, audience2: str, service: DataService = Depends(DataService)
):
    """Получить долю вхождения второй аудитории в первую по среднему весу метрики респондента.</br>
    Изменяемые параметры: Sex (1 - М, 2 - Ж), Age (0-100)"""
    return await service.calculate_percent(audience1, audience2)
