#!/bin/bash

set -e
OPENAPI_SPECS_URL=$1;

if [ -z "$OPENAPI_SPECS_URL" ]; then
  echo "Error: missing URL"
  echo "Usage: ./generate-client.sh http://localhost:8080/openapi.json"
  exit 1
fi

# Download openapi file
echo "Downloading openapi file"
curl -o openapi.json "$OPENAPI_SPECS_URL"

# Clean up openapi.json file (filter out unwanted endpoints)
echo "Cleaning up openapi file"
## Run the script twice: 1st time to keep tagged operations only, 2nd time to remove unused schemas
## removing unused schemas only works once the operations have already been filtered out
npx openapi-format ./openapi.json -o ./openapi.json  --filterFile ./openapi-filters.yaml
npx openapi-format ./openapi.json -o ./openapi.json  --filterFile ./openapi-filters.yaml
python openapi-fix.py

# Remove existing client folders, if any
rm -Rf ./dubo-api-client/
rm -Rf ../dubo/api_client

# Generate API client
if [ -d "./dubo-api-client" ]; then
  openapi-python-client update --path ./openapi.json
else
  openapi-python-client generate --path ./openapi.json
fi

# Move generated client and remove downloaded file
mv ./dubo-api-client/dubo_api_client ../dubo/api_client
rm -Rf ./dubo-api-client/
rm ./openapi.json
