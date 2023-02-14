# autonomusberry
## A folder containing several codes allowing you to interact with puredata from GPIO using python and OSC on Raspberry


The project is to use a Raspberry generating Farnell pd patches as an input for a modular we built and an arduino digital sequencer. The Modularduino repository contains all the code for the arduino sequencer. Chekc it out !  

------------------------

### GPIO input and OSC client
The rotary.py is a script controlling GPIO input (buttons, etc...) and sends OSC messages. Change the IP, port, name of the message and GPIO button address according to what you need

### OSC server and OLED display
The osc_server_concurrent.py allows you to receive OSC messages and display them on an oled screen pluged into the GPIO. Change de name of the message in the filter_handler and whatever you need to display

--------------------

All the code in the script is inspired by the examples scripts from pythonosc and gpiozero libraries. Thanks to them

A global_patch allow you to communicate with python scripts. Thanks to Andy Farnell for the content.

Enjoy and contact me if you need extra info ;)


