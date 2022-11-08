from subprocess import call
from os import getenv
import argparse

parser = argparse.ArgumentParser(description='Generate openapi SDKs.')
parser.add_argument('generator', help='name of openapi supported generator')
parser.add_argument('generator_tag')
parser.add_argument('openapi_file')
parser.add_argument('openapi_url')
parser.add_argument('config_file')
parser.add_argument('template_dir')
parser.add_argument('command_args', nargs = argparse.REMAINDER)

args = parser.parse_args()

cmd = "docker run -u 1001 --rm --workdir /github/workspace -v {workspace}:/github/workspace".format(workspace=getenv('GITHUB_WORKSPACE'))

cmd = "{cmd} openapitools/openapi-generator-cli:{generator_tag} generate".format(cmd=cmd, generator_tag=args.generator_tag)
cmd = "{cmd} -g {generator} -o /github/workspace/{generator}-client".format(cmd=cmd, generator=args.generator)

if args.openapi_url == "UNSET":
    cmd = "{cmd} -i /github/workspace/{openapi_file}".format(cmd=cmd, openapi_file=args.openapi_file)
else:
    cmd = "{cmd} -i {openapi_url}".format(cmd=cmd, openapi_url=args.openapi_url)

if args.config_file != "UNSET":
    cmd = "{cmd} -c /github/workspace/{config_file}".format(cmd=cmd, config_file=args.config_file)

if args.template_dir != "UNSET":
    cmd = "{cmd} -t /github/workspace/{template_dir}".format(cmd=cmd, template_dir=args.template_dir)

if args.command_args:
    cmd = "{cmd} {command_args}".format(cmd=cmd, command_args=' '.join(args.command_args))

# Call the command and return the exit code
exit(call(cmd, shell=True))
