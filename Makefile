lint:
	uv run ruff check .
install:
	uv sync --group dev
test:
	uv run pytest
test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml:coverage.xml
