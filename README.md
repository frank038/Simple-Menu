# Simple-Menu
A menu application.

V. 0.9 - Free to use and modify

Delete the file delete_me in the bookmarks folder before using this program.

This application lists all the applications installed in your system, also those added locally, through their desktop files.
Many options can be changed in its config file: theme, icon theme, position (if supported by the window manager), icon size, roundness, etc.
This program follows (most of) the freedesktop guidelines about the desktop files. Can launch terminal programs, e.g. Htop, if a terminal is found or setted in the config file. Local desktop files are used over system desktop files. A basic program is integrated for adding or modifying menu entries (optional). Searching, and many other things...

To bookmark or modify an entry, just right click on it.

Requirements:
- python3
- pyqt5
- python3 xdg
- optional, for rounded corners and shadow: a compositor

Just launch this program with the command:
./simplemenu.sh
or
python3 simplemenu.py

Can be executed under Xorg and under Wayland (no xwayland required).

This program can load the applications in two ways:
1) by parsing the desktop files at every launch
2) by creating a list (done automatically the first time, or manually); in this case the file must be recreated at every change in the menu: just execute createmenu.sh from terminal.

Without compositing option enabled
![This is an image](https://github.com/frank038/Simple-Menu/blob/main/screenshot1.png)

With compositing option enabled - the optional button for launching a menu editor is shown
![This is an image](https://github.com/frank038/Simple-Menu/blob/main/screenshot2.png)

The included program that adds or modifies menu entries.
![This is an image](https://github.com/frank038/Simple-Menu/blob/main/screenshot3.png)
