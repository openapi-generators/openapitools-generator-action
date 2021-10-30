#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

GENERATOR=$1
GENERATOR_TAG=$2
OPENAPI_FILE=$3
OPENAPI_URL=$4
CONFIG_FILE=$5

CMD="docker run -u 1001 --rm --workdir /github/workspace -v $GITHUB_WORKSPACE:/github/workspace"
CMD="$CMD openapitools/openapi-generator-cli:$GENERATOR_TAG generate"
CMD="$CMD -g $GENERATOR -o /github/workspace/$GENERATOR-client"

if [[ $OPENAPI_URL = "UNSET" ]]; then
  CMD="CMD -i /github/workspace/$OPENAPI_FILE"
else
  CMD="CMD -i $OPENAPI_URL";
fi

if [[ $CONFIG_FILE != "UNSET" ]]; then
  CMD="$CMD -c /github/workspace/$CONFIG_FILE"
fi

eval "$CMD"