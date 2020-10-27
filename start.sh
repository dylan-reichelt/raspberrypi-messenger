#!/bin/bash

../Documents/ngrok tcp 4556 > /dev/null & python3 ../Documents/raspberrypi-messengar/server/main.py localhost 4556 && killall ngrok
