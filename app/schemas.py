from pydantic import BaseModel


class GetPercentSchema(BaseModel):
    percent: float
