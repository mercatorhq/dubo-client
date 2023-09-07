#!/bin/bash

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
npx openapi-format ./openapi.json -o ./openapi.json  --filterFile ./openapi-filters.yaml
python openapi-fix.py

# Remove existing client folders, if any
rm -Rf ./dubo-api-client/
rm -Rf ./dubo_api_client/

# Generate API client
if [ -d "./dubo-api-client" ]; then
  openapi-python-client update --path ./openapi.json
else
  openapi-python-client generate --path ./openapi.json
fi

# Move generated client
mv ./dubo-api-client/dubo_api_client ./
rm -Rf ./dubo-api-client/
