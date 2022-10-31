#! /bin/sh.


sudo apt-get update
sudo apt-get install python3.8 python3-pip

pip install --upgrade twarc
twarc2 configure
