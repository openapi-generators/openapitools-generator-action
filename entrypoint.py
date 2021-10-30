from subprocess import call
from sys import argv
from os import getenv

(_, generator, generator_tag, openapi_file, openapi_url, config_file) = argv

cmd = f"docker run -u 1001 --rm --workdir /github/workspace -v {getenv('GITHUB_WORKSPACE')}:/github/workspace"
cmd = f"{cmd} openapitools/openapi-generator-cli:{generator_tag} generate"
cmd = f"{cmd} -g {generator} -o /github/workspace/{generator}-client"

if openapi_url == "UNSET":
    cmd = f"{cmd} -i /github/workspace/$OPENAPI_FILE"
else:
    cmd = f"{cmd} -i $OPENAPI_URL"

if config_file != "UNSET":
    cmd = f"{cmd} -c /github/workspace/$CONFIG_FILE"

# Call the command and return the exit code
exit(call(cmd, shell=True))
