#!/bin/bash

./ngrok tcp 4556 > /dev/null & python3 server/main.py localhost 4556 && killall ngrok
