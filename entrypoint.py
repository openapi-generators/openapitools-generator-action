from subprocess import call
from sys import argv
from os import getenv

(_, generator, generator_tag, openapi_file, openapi_url, config_file) = argv

cmd = f"docker run -u 1001 --rm --workdir /github/workspace -v {getenv('GITHUB_WORKSPACE')}:/github/workspace"
cmd = f"{cmd} openapitools/openapi-generator-cli:{generator_tag} generate"
cmd = f"{cmd} -g {generator} -o /github/workspace/{generator}-client"

if openapi_url == "UNSET":
    cmd = f"{cmd} -i /github/workspace/{openapi_file}"
else:
    cmd = f"{cmd} -i {openapi_url}"

if config_file != "UNSET":
    cmd = f"{cmd} -c /github/workspace/{config_file}"

# Call the command and return the exit code
exit(call(cmd, shell=True))
