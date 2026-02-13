.PHONY: install test clean

install:
	python -m venv .venv
	. .venv/bin/activate && pip install -r requirements.txt

test:
	. .venv/bin/activate && pytest

smoke_test:
	. .venv/bin/activate && pytest -m smoke

clean:
	rm -rf .venv