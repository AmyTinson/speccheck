# SpecCheck

An AI-powered tool for reviewing code changes against acceptance criteria and identifying testing gaps.

**Status:** Work in progress - AI integration coming soon.

## Tech Stack

Python · FastAPI · Pydantic · pytest · HTTPX

## Getting Started

Requires Python 3.10+

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Start the API:

```bash
python -m uvicorn app.main:app --reload
```

API documentation: http://localhost:8000/docs

Run tests:

```bash
python -m pytest -v
```

## Current Functionality

- Parse and structure acceptance criteria
- Validate API requests and responses with Pydantic
- REST endpoint (`POST /analyze`)
- Unit and API tests

## Roadmap

- [x] Python/FastAPI foundation
- [x] Criteria parsing and validation
- [x] Automated tests
- [ ] AI-powered criteria review
- [ ] Structured review findings
- [ ] GitHub PR integration
- [ ] Docker support

## Goal

Build a practical AI-assisted code review tool focused on requirements coverage, reliability, and developer experience.