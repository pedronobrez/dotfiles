# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

#     __   __                           __          __ 
#    / /  / /__ ____ ____  _______  ___/ /__  __ __/ / 
#   / _ \/ / _ `/ _ `/ _ \/ __/ _ \/ _  / _ \/ // / _ \
#  /_.__/_/\_,_/\_, /\___/_/  \___/\_,_/_//_/\_, /_//_/
#              /___/                        /___/      

from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal


# Autostart
import os
import subprocess
from libqtile import hook


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

mod = "mod1"
terminal = "termite"
browser = "google-chrome-stable"
file_manager = "nautilus"


keys = [
    # Rofi
    Key([mod], "space", lazy.spawn("rofi -combi-modi drun -font 'Mononoki Nerd Font 10' -show drun -icon-theme 'Papirus' -show-icons")),
    #Key([mod], "space", lazy.spawn("rofi -combi-modi drun -font 'Fira Code Nerd Font 24' -show drun -icon-theme 'Papirus' -show-icons -width 32")),

    # Lock Screen
    Key([mod],"l", lazy.spawn("betterlockscreen -l")),

    # Lock Screen + Suspend
    Key([mod], "s", lazy.spawn("betterlockscreen -s")),

    # Shutdown
    Key([mod, "shift"], "Delete", lazy.spawn("shutdown now")),

    # Reboot
    Key([mod, "shift"], "r", lazy.spawn("reboot")),

    # Volume
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -D pulse sset Master 5%+")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -D pulse sset Master 5%-")),
    Key([], "XF86AudioMute", lazy.spawn("amixer -D pulse sset Master toggle")),

    # Nightlight

    # Browser
    Key([mod], "b", lazy.spawn(browser)),

    # Notion
    Key([mod], "b", lazy.spawn("notion-app")),

    # File Manager
    Key([mod], "e", lazy.spawn(file_manager)),

    # VS Code
    Key([mod], "c", lazy.spawn("atom")),

    # Typora
    Key([mod], "t", lazy.spawn("typora")),

    # PDF Reader
    Key([mod], "p", lazy.spawn("evince")),

    # Discord
    Key([mod], "d", lazy.spawn("discord")),

    # Music
    Key([mod], "m", lazy.spawn("spotify")),

    # Github Desktop
    Key([mod], "g", lazy.spawn("github-desktop")),

    # Onlyoffice
    Key([mod], "o", lazy.spawn("onlyoffice-desktopeditors")),


    # Switch between windows
    Key([mod], "Tab", lazy.layout.down(), desc="Move focus down"),
    Key([mod, "shift"], "Tab", lazy.layout.up(), desc="Move focus up"),


    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod], "Up", lazy.layout.shuffle_up(), desc="Move window up"),


    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "l", lazy.layout.shrink(), desc="Grow window to the left"),
    Key([mod, "control"], "h", lazy.layout.grow(), desc="Grow window to the right"),
    # Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    # Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    # Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),


    # Launch terminal
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),


    # Toggle between different layouts as defined below
    Key([mod, "shift"], "l", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "BackSpace", lazy.shutdown(), desc="Shutdown Qtile"),

    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggles fullscreen"),

    Key([mod, "shift"], "space", lazy.window.toggle_floating()),

    Key([], "Print", lazy.spawn(
        "flameshot full -c"
    )),

    Key(["control"], "Print", lazy.spawn(
        "flameshot gui -p /home/blagorodnyh/screenshots/"
    )),
]

groups = [
    Group("১"),
    Group("২", matches=[Match(wm_class=['google-chrome'])]),
    Group("৩", matches=[Match(wm_class=['code', 'atom'])]),
    Group("৪", matches=[Match(wm_class=['notion-app', 'obsidian', 'typora'])]),
    Group("৫", matches=[Match(wm_class=['vlc'])]),
    Group("৬", matches=[Match(wm_class=['discord'])]),
    Group("৭", matches=[Match(wm_class=['Spotify', 'pavucontrol'])]),
    Group("৮", matches=[Match(wm_class=['gimp'])]),
    Group("৯", matches=[Match(wm_class=['simplescreenrecorder'])])
]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),

        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name, switch_group=True))
        ])

layout_theme = {"border_width":0,
"margin":8,
"border_focus": "009cdf",
"border_normal":"963d97"}

layouts = [
    #layout.Columns(border_focus_stack='#d75f5f'),
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    layout.MonadTall(**layout_theme),
    # layout.Tile(),
    # layout.Bsp(**layout_theme),
    layout.MonadWide(**layout_theme),
    # layout.Matrix(),
    # layout.RatioTile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    # layout.Floating(**layout_theme),
]

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=0,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    linewidth=0,
                    padding=5
                ),
                widget.GroupBox(
                    font="Mononoki Nerd Font",
                    fontsize=22,
                    highlight_method="block",
                    highlight_color=["191919"],
                    rounded=False,
                    padding_x=3,
                    padding_y=0,
                    active="#ffffff",
                    inactive="#6b6b6b",
                    this_current_screen_border="f531dc",
                    urgent_border="e23838",
                    disable_drag=True,
                    #margin_x=5,
                    spacing=8
                    #hide_unused=True
                ),
                widget.Sep(
                    linewidth=0,
                    padding=14
                ),
                widget.Prompt(
                    font="Mononoki Nerd Font",
                    fontsize=14,
                    foreground="009cdf"
                ),
                widget.Sep(
                    linewidth=0,
                    padding=10
                ),
                widget.WindowName(
                    font="Mononoki Nerd Font",
                    fontsize=13,
                    format=" {name} ",
                    #max_chars=50,
                    foreground="ffffff",
                    background="292d3e",
                    max_chars=77
                ),
                #widget.Spacer(),
                widget.Sep(
                    linewidth=0,
                    padding=5
                ),
                widget.Systray(
                    padding=3
                ),
                # widget.TextBox(
                #    text = "│",
                #    font="Mononoki Nerd Font",
                #    fontsize=18,
                #    padding=10,
                #    foreground="ffffff"
                # ),
                # widget.TextBox(
                #     text="    ",
                #     font="Mononoki Nerd Font",
                #     fontsize=14,
                #     foreground="5ebd3e"
                # ),
                # widget.OpenWeather(
                #     font="Mononoki Nerd Font",
                #     fontsize=14,
                #     format="{main_temp} °{units_temperature}",
                #     zip=21411,
                #     metric=True
                # ),
                # widget.TextBox(
                #     text="    ",
                #     font="Mononoki Nerd Font",
                #     fontsize=14,
                #     foreground="973999"
                # ),
                # widget.CPU(
                #     font="Mononoki Nerd Font",
                #     fontsize=14,
                #     foreground="ffffff",
                #     format="CPU {load_percent}%"
                # ),
                # widget.TextBox(
                #     text="  ",
                #     font="Mononoki Nerd Font",
                #     fontsize=14,
                #     foreground="ffb900"
                # ),
                # widget.Memory(
                #     font="Mononoki Nerd Font",
                #     fontsize=14,
                #     foreground="ffffff",
                #     # format="Mem {MemUsed: } /{MemTotal: }"
                # ),
                widget.TextBox(
                    text="    ",
                    font="Mononoki Nerd Font",
                    fontsize=14,
                    foreground="F531DC"
                ),
                widget.PulseVolume(
                    font="Mononoki Nerd Font",
                    fontsize=12,
                    foreground="ffffff",
                ),
                # widget.TextBox(
                #    text = "│",
                #    font="Mononoki Nerd Font",
                #    fontsize=14,
                #    padding=10,
                #    foreground="ffffff"
                # ),
                widget.TextBox(
                    text="    ",
                    font="Mononoki Nerd Font",
                    fontsize=14,
                    foreground = "F531DC"
                    # foreground="10F5DE"
                ),
                widget.Clock(
                    font="Mononoki Nerd Font",
                    fontsize=12,
                    format="%a - %b %d  |  %H:%M:%S",
                    # format="%a %m/%d/%Y  %d",
                    foreground="ffffff"
                ),
                # widget.TextBox(
                #     text="    ",
                #     font="Mononoki Nerd Font",
                #     fontsize=14,
                #     foreground="009cdf"
                # ),
                # widget.Clock(
                    # font="Mononoki Nerd Font",
                    # fontsize=14,
                    # #format="%a  %m/%d/%Y   %H : %M : %S",
                    # format="%H:%M:%S",
                    # foreground="ffffff"
                # ),
                widget.Sep(
                    linewidth=0,
                    padding=10
                )
            ],
            24,
            background = "#292d3e",
            opacity = 0.90,
            margin = [8,8,-3,8]
        ),
    ),
    # gradient: 3E9726 to 2EC5EF
    # yellow: f8aa0e
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
wmname = "LG3D"
