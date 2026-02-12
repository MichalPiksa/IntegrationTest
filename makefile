.PHONY: install test clean

install:
	python -m venv .venv
	. .venv/bin/activate && pip install -r requirements.txt

test:
	. .venv/bin/activate && pytest

clean:
	rm -rf .venv