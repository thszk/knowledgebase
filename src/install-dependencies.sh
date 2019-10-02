#! /usr/bin/env bash

if [ "$USER" != "root" ]; then
  echo "Without execute permission" && exit 1
fi

apt install python3-dev
apt install python3-pip
pip3 install setuptools
apt install python3-tk
pip3 install matplotlib==3.1.0
pip3 install networkx==2.3