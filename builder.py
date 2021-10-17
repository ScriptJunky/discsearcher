#!/usr/bin/env python

import argparse
import os
import re
import requests
import shutil
import stat
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
    'win32': 'win64.exe',
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

if platform == 'linux64' or platform == 'darwin64':
    os.chmod(package, 0o555)

print(f'File permissions of {package} have been set to {oct(os.stat(package).st_mode)[-3:]}')

# Let's go ahead and ship it off to bitbucket
uploadfile = {'files': open(package, 'rb')}
credentials = {
    'user': args.un,
    'password': args.pw
}

url = 'https://api.bitbucket.org/2.0/repositories/biscuits/discsearcher/downloads'
r = requests.post(url, auth=(args.un, args.pw), files=uploadfile)


# Clean up the remnants post build
os.remove(f'discsearcher-{version}-{platform}.spec')
shutil.rmtree('build', ignore_errors=True)
shutil.rmtree('dist', ignore_errors=True)
shutil.rmtree('__pycache__', ignore_errors=True)
