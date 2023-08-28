# This is a [justfile](https://github.com/casey/juste)

# set the default shell (to be safe)
set shell := ["zsh", "-uc"]

default:
	@just --list

test:
	poetry run pytest

build:
	poetry build

publish:
	poetry publish
