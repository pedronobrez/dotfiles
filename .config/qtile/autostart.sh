#!/bin/sh

feh --bg-scale ~/wallpapers/0007.jpg
xrdb -load ~/.Xresources
1password &

setxkbmap br -variant abnt2
picom &
dunst &

# mouse speed
xinput set-prop 12 303 -.47
