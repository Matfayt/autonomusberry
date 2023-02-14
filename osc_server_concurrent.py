from pythonosc.osc_server import AsyncIOOSCUDPServer
from pythonosc.dispatcher import Dispatcher
import asyncio

import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess
RST = None

DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0


# Load default font.
font = ImageFont.load_default()

#def filter_handler_rotary(address, *args):
    #print(f"{address}: {args}")
    #draw.text((x, top+45),     f"Rotary Value : {args}", font=font, fill=255)
    #disp.image(image)
    #disp.display()
    #time.sleep(.00001)

def filter_handler_number(address, *args):
    print(f"{address}: {args}")
    draw.text((x, top+25),     f"Patch number : {args}", font=font, fill=255)
    disp.image(image)
    disp.display()
    time.sleep(.1)
    
def filter_handler_dsp(address, *args):
    print(f"{address}: {args}")
    draw.text((x, top+35),     f"DSP: {args}", font=font, fill=255)
    disp.image(image)
    disp.display()
    time.sleep(1)

dispatcher = Dispatcher()
dispatcher.map("/dsp", filter_handler_dsp)
dispatcher.map("/number", filter_handler_number)
#dispatcher.map("/rotary", filter_handler_rotary)


ip = "127.0.0.1"
port = 3020

#to_print = args
IP = 1
i = 2
#range = [1, 2, 3]

async def loop():
    while True:
    # Draw a black filled box to clear the image
        draw.rectangle((0,0,width,height), outline=0, fill=0)
    # IP cmd
        cmd = "hostname -I | cut -d\' \' -f1"
        #cmd = "|cut -f 2 -d ' '"
        IP = subprocess.check_output(cmd, shell = True)
    # CPU usage cmd
        cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
        CPU = subprocess.check_output(cmd, shell = True )
    #CPU temp cmd
        cmd = "vcgencmd measure_temp | cut -f 2 -d '='"
        temp = subprocess.check_output(cmd, shell = True )
    # MEM usage cmd    
        cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
        MemUsage = subprocess.check_output(cmd, shell = True )
    
    # Draw text
        draw.text((x, top),       "IP: " + str(IP, 'utf-8'),  font=font, fill=255)
        draw.text((x, top+8),     str(CPU, 'utf-8') + " " + str(temp, 'utf-8'), font=font, fill=255)
        draw.text((x, top+16),    str(MemUsage, 'utf-8'),  font=font, fill=255)
        draw.text((x, top+55),   "<3puredata & raspi<3", font=font, fill=255)
       #draw.text((x, top+25),    str(Disk),  font=font, fill=255)
        disp.image(image)
        disp.display()
        time.sleep(.1)


       #print(f"Loop{i}")
        await asyncio.sleep(1)


async def init_main():
    server = AsyncIOOSCUDPServer((ip, port), dispatcher, asyncio.get_event_loop())
    transport, protocol = await server.create_serve_endpoint()  # Create datagram endpoint and start serving
    await loop()  # Enter main loop of program

    transport.close()  # Clean up serve endpoint


asyncio.run(init_main())
