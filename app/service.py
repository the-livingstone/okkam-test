import pandas as pd

from app.db import engine
from app.errors import RepresentativeError
from app.schemas import GetPercentSchema


class DataServiceError(RepresentativeError):
    pass


class DataService:

    async def calculate_percent(self, audience1: str, audience2: str):
        result1 = pd.read_sql(
            f"""
            SELECT AVG(weight) as avg_weight FROM some_research WHERE {audience1} GROUP BY respondent;
            """,
            engine,
        )
        common = pd.read_sql(
            f"""
            SELECT AVG(weight) as avg_weight FROM some_research WHERE {audience1} and {audience2} GROUP BY respondent;
            """,
            engine,
        )
        if awg_weight1 := result1.avg_weight.sum():
            percent = common.avg_weight.sum() / awg_weight1
        else:
            raise DataServiceError(title="Audience1 is empty")
        return GetPercentSchema(percent=percent)
