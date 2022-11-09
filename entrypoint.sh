#!/bin/bash

generator=$1
generator_tag=$2
openapi_file=$3
openapi_url=$4
config_file=$5
template_dir=$6
command_args=$7

cmd="docker run -u 1001 --rm --workdir /github/workspace -v $GITHUB_WORKSPACE:/github/workspace"
cmd="$cmd openapitools/openapi-generator-cli:$generator_tag generate"
cmd="$cmd -g $generator -o /github/workspace/$generator-client"

if [ "$openapi_url" = "UNSET" ]; then
    cmd="$cmd -i /github/workspace/$openapi_file"
else
    cmd="$cmd -i $openapi_url"
fi

if [ "$config_file" != "UNSET" ]; then
    cmd="$cmd -c /github/workspace/$config_file"
fi

if [ "$template_dir" != "UNSET" ]; then
    cmd="$cmd -t /github/workspace/$template_dir"
fi

if [ -n "$command_args" ]; then
    cmd="$cmd $command_args"
fi

echo "Final command: $cmd"

eval $cmd