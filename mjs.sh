#!/bin/bash
# ac: I got this script rpi forums user phl.
#first do 'sudo raspi-config' and activate camera module and reboot
#then sudo this script

echo "disable_camera_led=1"
echo "disable_camera_led=1" >> /boot/config.txt
echo "max_usb_current=1"
echo "max_usb_current=1" >> /boot/config.txt

# UPDATES
echo "updates.."
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install subversion libjpeg8-dev imagemagick libav-tools libv4l-dev cmake git -y

# DOWNLOAD MJPG-STREAMER
echo "install mjpg-streamer.."
cd /opt
sudo git clone https://github.com/jacksonliam/mjpg-streamer.git
cd mjpg-streamer/mjpg-streamer-experimental
export LD_LIBRARY_PATH=.
sudo make

# CREATE START SCRIPT
echo "create start script.."
sudo cat > /home/pi/run.sh << EOF
#!/bin/sh
#### CONFIG ##############
RESOLUTION_WIDTH="1296"
RESOLUTION_HEIGHT="972"
FPS="15"
QUALITY="10"
USERNAME=userxy
PASSWORD=pass1234
##########################
#ensure we are in the right path
cd /opt/mjpg-streamer/mjpg-streamer-experimental
export LD_LIBRARY_PATH=.
./mjpg_streamer -o "output_http.so -w ./www -c \$USERNAME:\$PASSWORD" -i "input_raspicam.so -fps \$FPS -x \$RESOLUTION_WIDTH -y \$RESOLUTION_HEIGHT -q \$QUALITY"
EOF

# MAKE IT EXECUTEABLE AND MOVE
echo "make start script executeable.."
sudo chmod +x /home/pi/run.sh
sudo mv /home/pi/run.sh /opt/mjpg-streamer/mjpg-streamer-experimental

# LINK SCRIPT IN STARTUP
echo "link start script in rc.local.."
sudo sed -i '$i/opt/mjpg-streamer/mjpg-streamer-experimental/run.sh' /etc/rc.local

sudo reboot
