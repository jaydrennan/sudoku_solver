init:
	pyenv install 3.8.3 -s
	pyenv virtualenv 3.8.3 sudoku-3.8.3
	pyenv local sudoku-3.8.3
	pip install pip --upgrade
	pip install -r requirements.txt
	pyenv which python

format:
	black .

af: format linter

test:
	pytest tests/

build:
	DOCKER_BUILDKIT=1 docker build -t jdrennan/sudoku:latest .

run: build
	docker run -p 5000:5000 jdrennan/sudoku

linter:
	flake8 --ignore=E203,E501,W503 .

freeze: requirements/requirements.in requirements/dev_requirements.in
	pip-compile --output-file=requirements/requirements.txt requirements/requirements.in
	pip-compile --output-file=requirements/dev_requirements.txt requirements/dev_requirements.in