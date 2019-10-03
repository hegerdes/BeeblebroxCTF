#!/bin/bash


if [ $# -eq 0 ]; then
    echo "Please use $0 ext or $0 com"
fi
if [ "$1" = "com" ]; then
    tar cfv ../level_04/Game.tar ../level_04/SpaceShooter
    gzip ../level_04/Game.tar
fi


if [ "$1" = "ext" ]; then
    gunzip ../level_04/Game.tar.gz
    tar xfv ../level_04/Game.tar -C ../level_04
    rm ../level_04/Game.tar
fi
