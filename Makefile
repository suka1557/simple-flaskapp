VENV_NAME = bmi_env
PYTHON = $(VENV_NAME)/bin/python3
PIP = $(VENV_NAME)/bin/pip
REQUIREMENTS = requirements.txt

venv:
	python3 -m venv $(VENV_NAME)
	. ./$(VENV_NAME)/bin/activate
	$(PIP) install -U pip
	$(PIP) install -r $(REQUIREMENTS)

test:
	$(PYTHON) -m pytest -v -cov

run:
	$(PYTHON) app.py

deactivate:
	deactivate

clean:
	rm -rf __pycache__
	rm -rf $(VENV_NAME)