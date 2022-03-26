#!/bin/sh

feh --bg-scale ~/wallpapers/5120x2880.png
xrdb -load ~/.Xresources

setxkbmap br -variant abnt2
picom &
dunst &

# mouse speed
xinput set-prop 12 303 -.47
