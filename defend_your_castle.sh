#!/bin/bash

#https://www.youtube.com/watch?v=dfRcQHM9F4M

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
cd "$DIR"

python defend_your_castle1.py
python defend_your_castle2.py &
timeout 95 python defend_your_castle3.py
