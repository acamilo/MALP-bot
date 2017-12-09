from flask import Flask, g, render_template
from netifaces import interfaces, ifaddresses, AF_INET
import os

app = Flask(__name__,static_folder="static")


#Movement Command
@app.route('/move/<pos_x>/<pos_y>')
def index(pos_x,pos_y):
  setVelocity(int(pos_x),int(pos_y))
  #print "Xpos: %s \t Ypos: %s" % (pos_x,pos_y)
  return "{\"result\":\"ok\"}"


#serve our static files
@app.route('/<path:filename>')
def serve_static(filename):
  return app.send_static_file(filename)

# make sure index is served for '/'  
@app.route('/')
def serve_index():
  return render_template('index.html', myip = getWLANIP())


#wifi ip addr get helper func
def getWLANIP():
  return [i['addr'] for i in ifaddresses("wlan0").setdefault(AF_INET, [{'addr':'No IP addr'}] )][0]

leftIO    = 12
rightIO   = 13
leftzero  = 155
rightzero = 156
k = 0.2

#Get joystick X and Y and set a motor velocity
def setVelocity(x,y):
  leftvel  = k*(x-y) + leftzero
  rightvel = -1*k*(x+y) + rightzero
  os.system("gpio -g pwm %d %d"%(leftIO,leftvel))
  os.system("gpio -g pwm %d %d"%(rightIO,rightvel))

if __name__ == '__main__':
  os.system("gpio -g mode %d pwm"%(leftIO))
  os.system("gpio -g mode %d pwm"%(rightIO))
  os.system("gpio pwm-ms")
  os.system("gpio pwmc 192")
  os.system("gpio pwmr 2000")
  app.run(host='0.0.0.0', port=80)
