import argparse
import os
import re
import requests
import shutil
import sys
import PyInstaller.__main__

parser = argparse.ArgumentParser()
parser.add_argument('--un', help=argparse.SUPPRESS)
parser.add_argument('--pw', help=argparse.SUPPRESS)
args = parser.parse_args()

if not args.un:
    print('Missing username for bitbucket POST!')
    sys.exit(1)

if not args.pw:
    print('Missing password for bitbucket POST!')
    sys.exit(1)


# Let's get our platform information
platdict = {
    'win32': 'windows64.exe',
    'darwin': 'darwin64',
    'linux': 'linux64'
}

platform = sys.platform

for key in platdict.keys():
    platform = platform.replace(key, platdict[key])


# Let's get our current version number
cwd = os.getcwd()
toolpath = cwd + '/discsearcher.py'
with open('discsearcher.py') as f:
    version = re.search('\d{4}.\d{3}', f.read())
    version = 'v' + version.group()
    f.close()


# Building time!
PyInstaller.__main__.run([
    f'--name=discsearcher-{version}-{platform}',
    '-F',
    os.path.join('my_package', toolpath)
])
package = cwd + f'/dist/discsearcher-{version}-{platform}'


# Let's go ahead and ship it off to bitbucket
uploadfile = {'file': open(package, 'rb')}
credentials = {
    'username': args.un,
    'password': args.pw
}

print(args.un, args.pw)
url = 'https://api.bitbucket.org/2.0/repositories/biscuits/discsearcher/downloads'
r = requests.post(url, data=credentials, files=uploadfile)
print(r.text, r.status_code)
