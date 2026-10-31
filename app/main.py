from fastapi import FastAPI

from .analyzer import analyze_criteria
from .models import AnalysisResult, AnalyzeRequest

app = FastAPI()


@app.post("/analyze", response_model=AnalysisResult)
def analyze(request: AnalyzeRequest):
    criteria = request.criteria
    return analyze_criteria(criteria)
