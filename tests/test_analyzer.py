from app.analyzer import analyze_criteria


def test_analyze_criteria():
    criteria = [
        "Users can upload PDFs",
        "Maximum upload size is 10MB",
    ]

    result = analyze_criteria(criteria)

    assert result.total == 2
    assert result.criteria[0].id == 1
    assert result.criteria[1].text == criteria[1]


def test_analyze_empty_criteria():

    result = analyze_criteria([])

    assert result.total == 0
    assert result.criteria == []
