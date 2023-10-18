dubo
====

The Dubo SDK lets you interact with databases and data documentation via natural language. Use it with internal tools like Slackbots, within your company's ChatGPT plugin, or in your product directly.

To get started, check out the [documentation](https://docs.dubo.gg).

## Developing for the Dubo SDK

### Generating the API Client

An api client can be generated to access the dubo API, it is located in the `/dubo/api_client` folder:

```shell
just generate-api-client
```

More info can be found in the README file inside the `api-client-generator` folder.

### Generating Documentation

```shell
just generate-doc
```
