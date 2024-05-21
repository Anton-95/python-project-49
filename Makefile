install: # poetry install
	poetry install

brain-games: # start game
	poetry run brain-games

build: # project building
	poetry build

publish: # project publication
	poetry publish --dry-run

package-install: # project install
	python3 -m pip install --user dist/*whl
