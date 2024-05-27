
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

package-reinstall: #reinstall project
	python3 -m pip install --user --force-reinstall dist/*whl

linter: #start linter
	poetry run flake8 brain_games
