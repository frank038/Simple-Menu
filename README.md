# Simple-Menu
A menu application.

V. 0.6 - Free to use and modify

Delete the file delete_me in the bookmarks folder before using this program.

This application lists all the applications installed in your system, also those added locally.
Many options can be changed in its config file: theme, icon theme, position (if supported by the window manager), icon size, roundness, etc.
This program follows the freedesktop guidelines about the desktop files. Can launch terminal programs, e.g. Htop, if a terminal is found or setted in the config file. Local desktop file are used over system desktop files. Integrated (optional) basic program for adding or modifying menu entries. And many other things...

Requirements:
- python3
- pyqt5
- python3 xdg
- optional, for rounded corners and shadow: a compositor

Just launch this program with the command:
./simplemenu.sh
or
python3 simplemenu.py

Can be executed under Xorg and under Wayland.

Without compositing option enabled
![This is an image](https://github.com/frank038/Simple-Menu/blob/main/screenshot1.png)

With compositing option enabled - the optional button for launching a menu editor is shown
![This is an image](https://github.com/frank038/Simple-Menu/blob/main/screenshot2.png)

The included program that adds or modifies menu entries.
![This is an image](https://github.com/frank038/Simple-Menu/blob/main/screenshot3.png)
