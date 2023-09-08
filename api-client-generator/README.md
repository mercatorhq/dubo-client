# API CLIENT GENERATION

## Prerequisites

- npx: `npm install -g npx`
- openapi-python-client: `pip install openapi-python-client`

n.b. at the moment, `openapi-python-client` does not support OpenAPI 3.1 and instead the following should be used:

`pip install git+https://github.com/staticdev/openapi-python-client.git@feature/enable-openapi-3.1.0`

once a new version of `openapi-python-client` that supports OpenAPI 3.1 is released, this can be changed

## Execution

To generate the openapi python client, run the following command:

```shell
./generate-client.sh http://localhost:8080/openapi.json
```

## Details

To generate the api client, the following steps happen:

1. The openapi.json file is downloaded from the dubo-api
2. Using [openapi-format](https://www.npmjs.com/package/openapi-format) the operations that do not have the "keyed_api"
   tag are filtered out
3. Because the file that `openapi-format` generates contains some invalid array definitions, `openapi-fix.py` fixes
   these issues
4. The existing `/dubo/api_client` folder is removed, if it exits
5. Using `openapi-python-client`, the dubo api client is generated
6. The generated folder is moved and renamed (the generators creates it in a sub-folder)
