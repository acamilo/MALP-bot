from flask import Flask, g, render_template
from netifaces import interfaces, ifaddresses, AF_INET

app = Flask(__name__,static_folder="static")


#Movement Command
@app.route('/move/<pos_x>/<pos_y>')
def index(pos_x,pos_y):
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
  return [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
