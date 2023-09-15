# Command runner for dubo sdk
# This is a [justfile](https://github.com/casey/juste)

# set the default shell (to be safe)
set shell := ["zsh", "-uc"]

# load vars found in .env
set dotenv-load

default:
	@just --list

generate-api-client:
	@cd api-client-generator && ./generate-client.sh "${DUBO_BASE_URL:-http://localhost:8080}/openapi.json"

generate-doc:
	@pydoc-markdown
