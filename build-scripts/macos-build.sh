#!/bin/bash

if [ "$#" -lt 2 ]]; then
    echo "Missing username and password!"
    exit 1
else
    rm -fr ~/build
    mkdir ~/build
    cp ~/git/discsearcher/discsearcher.py ~/build/
    cd ~/build
    pyinstaller -F discsearcher.py
    VERSION=$(grep vnum.= discsearcher.py | cut -d= -f2 | tr -d ' ')
    cd dist/
    zip discsearcher-v$VERSION-darwin64.zip discsearcher
    curl --verbose -s -u $1:$2 -X POST https://api.bitbucket.org/2.0/repositories/biscuits/discsearcher/downloads -F files=@discsearcher-v$VERSION-darwin64.zip
fi     
