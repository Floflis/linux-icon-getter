#!/usr/bin/env python3
#from kiri's StackOverflow answer: https://askubuntu.com/a/400243 ; answer based in Stefano Palazzo's original code/answer here: https://askubuntu.com/a/52432

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import sys


if len(sys.argv) > 1:
    icon_name = sys.argv[1]
else:
    icon_name = input("Icon name (case sensitive): ")
if icon_name:
    theme = Gtk.IconTheme.get_default()
    found_icons = []
    for res in range(0, 512, 2):
        icon = theme.lookup_icon(icon_name, res, 0)
        if icon:
            found_icons.append(icon.get_filename())

if found_icons:
    print(found_icons[-1])
else:
    print(icon_name, "was not found")

