#!/bin/bash

clear
echo "Installing REXE Hacker Store..."

pkg update -y
pkg upgrade -y

pkg install git -y
pkg install python -y
pkg install python-pip -y
pkg install php -y
pkg install curl -y
pkg install wget -y
pkg install nmap -y
pkg install clang -y
pkg install make -y
pkg install golang -y

pip install requests
pip install colorama

echo ""
echo "Installation Complete!"
echo "Run Tool: python rexe.py"
