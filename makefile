ENV = env
PYTHON = $(ENV)/bin/python3
PIP = $(ENV)/bin/pip

default: 
	@cat makefile

env:
	python3 -m venv env; . env/bin/activate; pip install --upgrade pip

update: env
	$(PIP) install -r requirements.txt
#	. env/bin/activate; pip install -r requirements.txt

lint: update
	$(PYTHON) -m pylint bin/ tests/
#	. env/bin/activate; pylint bin/clean_ids.py

test: lint
	$(PYTHON) -m pytest -vvx tests
#	. env/bin/activate; pytest -vvx tests

test_enrich:
	@. env/bin/activate && cat mock_transcripts.jsonl | python -u bin/enrich_transcripts.py | python bin/validate_schema.py