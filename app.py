from flask import Flask, render_template, Response, request, jsonify, redirect, url_for
from pprint import pprint
import requests
import random
import time

app = Flask(__name__, static_folder='static')
port=8000

print('\n\n🤖 Basic Flask Example 🤖\n')
print('View the dashboard. Go to:')
print(f'🏠 http://0.0.0.0:{port}/ in your browser\n\n')

# manages dashboard display and form submission
@app.route('/', methods=["POST","GET"])
def home():
    if request.method == "POST":
        data = request.form.to_dict()
        print('\n🚨 You Just Submitted a Form! 🚨')
        pprint(data)
        print("")
    return render_template('index.html')

# video recording controls continued
@app.route('/do-something')
def do_something():
    print('\n🏁 You just clicked a button! 🏁\n')
    return ''

@app.route('/toggle', methods=['POST']) 
def toggled_status():
    if request.method == 'POST':
        data = request.form.to_dict()
        if data['status'] == 'true':
            status = "✅ The toggle is on!"
        else:
            status = "🔴 The toggle is off."
        print("\n", status, "\n")
        return status

@app.route('/mouse_down') 
def mousedown():
    global down
    down = True
    print('\n')
    while down:
        print(random.randint(0,10))
        time.sleep(0.01)
    print('\n')
    return ''

@app.route('/mouse_up')
def mouseup():
    global down
    down = False
    print("\n😮 You let go of the button!\n")
    return ''

if __name__ == '__main__':
    # start the app
    app.run(host='0.0.0.0', port=port, debug=False)

