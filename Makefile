init:
	pyenv install 3.8.3 -s
	pyenv virtualenv 3.8.3 sudoku-3.8.3
	pyenv local sudoku-3.8.3
	pip install pip --upgrade
	pip install -r requirements.txt
	pyenv which python

format:
	black .

af: format

test:
	pytest tests/

build:
	DOCKER_BUILDKIT=1 docker build -t jdrennan/sudoku:latest .

run: build
	docker run -p 5000:5000 jdrennan/sudoku

