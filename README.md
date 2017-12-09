# MALP-bot

## Install
1. Run camera setup script
2. apt-get install [pkglist]
3. test by running start.sh
4. add ''' /home/pi/MALP-bot/run.sh ''' to /etc/rc.local
5. Make FS read only

## Todo
* [x] Streaming Webcam
   * [x] Find resolution/framerate/latency sweet-spot
  * [x] Start server on boot
* Control Webpage
  * [x] Touchpad/Mouse joystick
  * [x] periodic GET requests with stick x/y
  * [x] embedded live stream
  * [x] "HUD" overlay
  * Display Battery voltage
* RPI Backend
  * [x] Accept Inputs using flask
  * [x] GPIO PWM Servo Control. x/y to diff drive.
  * [x] Serve static Files
  * [x] Embedd Camera feed w/o hardcoding IP addr
  * battery voltage sense
  * start server on system boot
  * read-only filesystem
