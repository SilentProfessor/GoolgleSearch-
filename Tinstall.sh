#/bin/bash

apt upgrade -y
apt update -y
apt install python
pip install googlesearch-python

python GSE.py
