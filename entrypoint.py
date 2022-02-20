from subprocess import call
from sys import argv
from os import getenv

(_, generator, generator_tag, openapi_file, openapi_url, config_file, template_dir, *args) = argv

cmd = f"docker run -u 1001 --rm --workdir /github/workspace -v {getenv('GITHUB_WORKSPACE')}:/github/workspace"
cmd = f"{cmd} openapitools/openapi-generator-cli:{generator_tag} generate"
cmd = f"{cmd} -g {generator} -o /github/workspace/{generator}-client"

if openapi_url == "UNSET":
    cmd = f"{cmd} -i /github/workspace/{openapi_file}"
else:
    cmd = f"{cmd} -i {openapi_url}"

if config_file != "UNSET":
    cmd = f"{cmd} -c /github/workspace/{config_file}"

if template_dir != "UNSET":
    cmd = f"{cmd} -t /github/workspace/{template_dir}"

if args:
    cmd = f"{cmd} {' '.join(args)}"

# Call the command and return the exit code
exit(call(cmd, shell=True))
