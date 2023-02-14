from threading import Event
from gpiozero import RotaryEncoder, RGBLED, Button
from signal import pause
from pythonosc.udp_client import SimpleUDPClient

	#rotary button setup
rotor = RotaryEncoder(16, 20, wrap=True, max_steps=180)
rotor.steps = -50
btn = Button(21, pull_up=True)
done = Event()

	#OSC setup
ip = "127.0.0.1"
port = 3010

client = SimpleUDPClient(ip, port)


def change_value():
	# Scale the rotor steps (-180..180) to 0..1
	hue = (rotor.steps + 50) / 100
	print (hue)
	client.send_message("/rotary", hue)

def button_clicked():
	print('button clicked')
	client.send_message("/change", 1)
def button_held():
	print('button held')
	client.send_message("/pause", 1)

print('Select a color by turning the knob')
rotor.when_rotated = change_value
print('Push the button to see the HTML code for the color')
btn.when_released = button_clicked
print('Hold the button to exit')
btn.when_held = button_held
done.wait()
