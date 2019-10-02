#! /usr/bin/env bash

if [ "$USER" != "root" ]; then
  echo "Without execute permission" && exit 1
fi

apt update
apt upgrade -y 

apt install python3-dev -y
apt install python3-pip -y
pip3 install setuptools
apt install python3-tk -y
pip3 install matplotlib==3.1.0
pip3 install networkx==2.3