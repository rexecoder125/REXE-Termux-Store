#!/bin/bash

echo ""
echo "🛠 Installing REXE Termux Tool Store..."
echo ""

pkg update -y
pkg upgrade -y
pkg install python git -y

pip install -r requirements.txt

echo ""
echo "✅ Installation Complete!"
echo "Run: python rexe.py"
echo ""
