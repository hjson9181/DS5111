default: 
	@cat makefile

env:
	python3 -m venv env; . env/bin/activate; pip install --upgrade pip

update: env
	. env/bin/activate; pip install -r requirements.txt

lint: env
	. env/bin/activate; pylint bin/clean_ids.py

test: env
	. env/bin/activate; make lint && pytest -vv test
