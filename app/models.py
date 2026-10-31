from pydantic import BaseModel


class Criterion(BaseModel):
    id: int
    text: str


class AnalysisResult(BaseModel):
    total: int
    criteria: list[Criterion]


class AnalyzeRequest(BaseModel):
    criteria: list[str]
