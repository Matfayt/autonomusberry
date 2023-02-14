# autonomusberry
A folder containing several codes allowing you to interact with puredata from GPIO using python and OSC on Raspberry

----------------------

The project is to use a Raspberry generating Farnell pd patches as an input for a modular we built and an arduino digital sequencer 

The rotary.py is a script controlling GPIO input (buttons, etc...) and sends OSC messages.

The osc_server_concurrent.py allows you to receive OSC messages and display them on an oled screen pluged into the GPIO

A global_patch allow you to communicate with python scripts

Enjoy ;)
