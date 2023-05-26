.PHONY: init clean dist test install upload
.DEFAULT_GOAL := init

init:
	poetry install
	poetry run pip install --upgrade setuptools wheel twine

clean:
	poetry run test -d dist && poetry run rm -rf dist
	poetry run rm -rf *.egg-info

dist: clean
	poetry build

test: dist
	poetry run pip install dist/helm_compose-$(shell poetry version -s).whl

install: dist
	poetry install

install-prod: dist
	poetry install --no-dev

upload: dist
	poetry publish

# Additional Commands

pytest:
	poetry run pytest

mypy:
	poetry run mypy .

flake8:
	poetry run flake8 .

black:
	poetry run black .

pre-commit:
	poetry run pre-commit run --all-files

coverage:
	poetry run coverage run -m pytest
	poetry run coverage report

sphinx:
	poetry run sphinx-build docs docs/_build

isort:
	poetry run isort .

sphinx-autodoc-typehints:
	poetry run sphinx-autodoc-typehints .

pre-commit-hooks:
	poetry run pre-commit install

blacken-docs:
	poetry run black docs

integrated:
	poetry run pytest
	poetry run mypy .
	poetry run flake8 .
	poetry run black .
	poetry run pre-commit run --all-files
	poetry run coverage run -m pytest
	poetry run coverage report
	poetry run sphinx-build docs docs/_build
	poetry run isort .
	poetry run sphinx-autodoc-typehints .
	poetry run pre-commit install
	poetry run black docs

# GitHub Tagging Commands

get-last-tag = $(shell git describe --abbrev=0 --tags 2>/dev/null)
get-version = $(if $(call get-last-tag),$(patsubst v%,%,$(call get-last-tag)),0.0.0)

tag-patch-DEPRECATED:
	poetry version patch
	$(call create-tag,$(call get-version),$(shell poetry version -s))

tag-minor-DEPRECATED:
	poetry version minor
	$(call create-tag,$(call get-version),$(shell poetry version -s))

tag-major-DEPRECATED:
	poetry version major
	$(call create-tag,$(call get-version),$(shell poetry version -s))

define create-tag
	@if [ "$(strip $(1))" = "0.0.0" ]; then \
		git tag -a v$(strip $(2)) -m "Version $(strip $(2))"; \
	else \
		git tag -a v$(strip $(2)) -m "Version $(strip $(2))" $(strip $(1)); \
	fi
	git push origin v$(strip $(2))
endef

# bump patch and create git tag with version from poetry
bump-patch:
	poetry version patch
	

bump-minor:
	poetry version minor

bump-major:
	poetry version major