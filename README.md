# openapitools-generator-action
Generate a client library from an OpenAPI document using the [OpenAPITools Generator](https://github.com/OpenAPITools/openapi-generator)

## Inputs

### `generator`

The generator you wish to use (i.e. the language you want to generate a client library for). See [the official list of supported languages/generators](https://openapi-generator.tech/docs/generators) and [the openapi-generator repo](https://github.com/OpenAPITools/openapi-generator) for more info.

### `config-file`

The path to the config file to be used with `openapi-generator`. Paths that do not start with `/` are assumed to be relative to the root of the repository. 

For information on what can be configured, see [the page on customization in the repo](https://github.com/OpenAPITools/openapi-generator/blob/master/docs/customization.md).

### `openapi-file`

The path to the OpenAPI document (both JSON and YAML are supported). Defaults to "openapi.json" (i.e. a file in the current directory called openapi.json). Paths that do not start with `/` are assumed to be relative to the root of the repository.

### `openapi-url`

The URL to load the OpenAPI document from. If set, `openapi-file` will be ignored.

### `docker-repository`

The Docker repository uses as source for  `docker-image`. Defaults to `docker.io`.

### `docker-image`

The Docker image used by the generator. Defaults to `openapitools/openapi-generator-cli`.

### `generator-tag`

The Docker tag of the openapitools/openapi-generator-cli image to use. See [the DockerHub repo](https://hub.docker.com/r/openapitools/openapi-generator-cli/tags) for available tags.

### `template-dir`

The path to the folder containing the template files. Paths that do not start with `/` are assumed to be relative to the root of the repository. 

See user-defined [templates](https://openapi-generator.tech/docs/templating#modifying-templates) via options.

### `command-args`

Additional arguments to pass through to the [generate](https://openapi-generator.tech/docs/usage#generate) command.

## Outputs

No outputs are returned. The generated client is placed in the current directory. The name of the package (unless configured differently) will be `generator-name-client` where "generator-name" is (unsurprisingly) the name of the generator used to generate the client.

## Example usage
```yaml
jobs:
  generate-angular-client:
    runs-on: ubuntu-latest
    name: Example
    steps:

      # Checkout your code
      - name: Checkout
        uses: actions/checkout@v2

      # Generate your OpenAPI document (if you don't write it manually)

      # Use the action to generate a client package
      # This uses the default path for the openapi document and thus assumes there is an openapi.json in the current workspace.
      - name: Generate Angular Client
        uses: openapi-generators/openapitools-generator-action@v1
        with:
          generator: typescript-angular
          config-file: angular-generator-config.yml

      # Do something with the generated client (likely publishing it somewhere)
      - name: Do something with the client
        run: |
          cd typescript-angular-client
```

## Template example usage
```yaml
jobs:
  generate-angular-client:
    runs-on: ubuntu-latest
    name: Example
    steps:

      # Checkout your code
      - name: Checkout
        uses: actions/checkout@v2

      # Generate your OpenAPI document (if you don't write it manually)

      # Use the action to generate a client package
      # This uses the default path for the openapi document and thus assumes there is an openapi.json in the current workspace.
      - name: Generate Angular Client
        uses: openapi-generators/openapitools-generator-action@v1
        with:
          generator: typescript-angular
          config-file: angular-generator-config.yml
          template-dir: templates/typescript-angular

      # Do something with the generated client (likely publishing it somewhere)
      - name: Do something with the client
        run: |
          cd typescript-angular-client
```
