lint:
	uv run ruff check .
install:
	uv sync --group dev
