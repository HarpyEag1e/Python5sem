#!/bin/bash

touch ~/info.txt
filepath=~/'info.txt'

cat > $filepath << EOF
Hello, $(whoami)
time: $(date)
os: $(uname -s)
home directory: $HOME
memory: $(df -lh --output=used ~ | grep -v Used) (used), $(df -lh --output=avail ~ | grep -v Avail) (free)
num folders: $(tree -dL 1 ~ | tail -n 1 | cut -d ' ' -f 1)
num files: $(tree ~ | tail -n 1 | cut -d ' ' -f 3)
EOF
