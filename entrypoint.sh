#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

generator_name=$1
config_file=$2
openapi_file=$3
openapi_url=$4

document=$openapi_url && [[ $openapi_url = "UNSET" ]] && document="/github/workspace/${openapi_file}"
docker run -u 1001 --rm --workdir /github/workspace -v "$GITHUB_WORKSPACE":"/github/workspace" \
  openapitools/openapi-generator-cli generate \
  -i "$document" \
  -g "$generator_name" \
  -c "/github/workspace/$config_file" \
  -o "/github/workspace/${generator_name}-client"
