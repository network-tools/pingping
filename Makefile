.PHONY: help install test lint format clean testiq coverage html-report all

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies with uv
	uv sync --all-extras

test: ## Run tests with pytest
	uv run pytest

test-verbose: ## Run tests with verbose output
	uv run pytest -v

lint: ## Run ruff linter
	uv run ruff check .

lint-fix: ## Run ruff linter with auto-fix
	uv run ruff check . --fix

lint-unsafe-fix: ## Run ruff linter with unsafe auto-fixes
	uv run ruff check . --fix --unsafe-fixes

format: ## Format code with black
	uv run black .

format-check: ## Check code formatting without changes
	uv run black --check .

testiq: ## Run testiq analysis (skips similarity checks)
	uv run pytest --testiq-output=testiq_coverage.json
	uv run testiq analyze testiq_coverage.json --threshold 0.96

testiq-score: ## Get test quality score
	uv run pytest --testiq-output=testiq_coverage.json
	uv run testiq quality-score testiq_coverage.json

testiq-html: ## Generate testiq HTML report
	uv run pytest --testiq-output=testiq_coverage.json
	uv run testiq analyze testiq_coverage.json --threshold 0.96 --format html --output testiq_report.html
	@echo "Report generated: testiq_report.html"

coverage: ## Run tests with coverage report
	uv run pytest --cov=pingping --cov-report=term-missing

html-report: ## Generate HTML coverage report
	uv run pytest --cov=pingping --cov-report=html
	@echo "Report generated: htmlcov/index.html"

clean: ## Clean up generated files
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -rf .ruff_cache
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info
	rm -f coverage.xml coverage.json testiq_coverage.json testiq_report.html
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete

all: lint-fix format test ## Run linter, formatter, and tests

ci: lint format-check test testiq ## Run all CI checks locally

.DEFAULT_GOAL := help
