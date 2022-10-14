from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask import Flask, render_template, Response, request, jsonify, redirect, url_for
import requests
import time
import random



app = Flask(__name__, static_folder='static')
port=8000

# output link for webapp
print('\n\n🤖 Pi-Vision 🤖\n')
print('Log in to Pi-Vision. Go to:')
print('🏠 http://0.0.0.0:'+ str(port) +'/ if local')
# get the external ip of the raspberry pi
ip = requests.get('https://api.ipify.org').text
print('🌎 http://' + ip + ':'+ str(port) +'/ if remote (most users)')
print('')

# - - - - - - - - - - - - - - - LOG IN MANAGEMENT START - - - - - - - - - - - - - - - - - - - -

# video recording controls continued
@app.route('/do-something')
def do_something():
    print('\n🏁 I just did something!\n')
    return ''

# - - - - - - - - - - - APP PAGES START - - - - - - - - - - - - - - - - -

# full robotic arm control panel
@app.route('/', methods=["POST","GET"])
#@login_required
def home():
    if request.method == "POST":
        print('')
        first_name = request.form.get("firstname")
        print('First Name:', first_name)
        last_name = request.form.get("lastname")
        print('Last Name:', last_name)
        age = request.form.get("age")
        print('Age:', age)
        print('')

    return render_template('index.html')

status = 'on'
@app.route('/get_toggled_status') 
def toggled_status():
    global status
    if status == 'off':
        status = 'on'
    else:
        status = 'off'
    
    print('\nToggle Status:', status, '\n')
    return status



down = False
@app.route('/mousedown') 
def mousedown():
    global down
    down = True
    while down:
        print(random.randint(0,10))
        time.sleep(0.01)
    return ''

@app.route('/mouseup')
def mouseup():
    global down
    down = False
    return ''




# - - - - - - - - - - - APP PAGES END - - - - - - - - - - - - - - - - -

# - - - - - - - - - - RETA APP START - - - - - - - - - - - - - - - -
if __name__ == '__main__':
    # start the app
    app.run(host='0.0.0.0', port=port)

