FROM ubuntu:latest

RUN apt-get update && apt-get install -y curl python3 python3-pip git zip
RUN pip3 install numpy bs4 requests regex tabulate pandas exrex lxml pyinstaller
RUN git clone https://bitbucket.org/biscuits/discsearcher
