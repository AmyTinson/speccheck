from .models import AnalysisResult

criteria = [
    "Users must be able to upload PDF files",
    "Uploads must be limited to 10MB",
    "Users should receive an error for invalid files",
]


def analyze_criteria(criteria: list[str]) -> AnalysisResult:
    total = len(criteria)
    formatted = [dict(id=idx, text=val) for idx, val in enumerate(criteria, start=1)]
    analyzed = dict(total=total, criteria=formatted)
    result = AnalysisResult.model_validate(analyzed)

    return result
    # pass
