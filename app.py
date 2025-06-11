from flask import Flask, render_template
from media_control import play_pause, next_track, prev_track, stop
from volume_control import volume_up, volume_down, set_system_volume, get_system_volume
 

import logging
logging.basicConfig(filename="error.log", level=logging.ERROR)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

 

@app.route("/media/<action>")
def media_control(action):
    if action == "play":
        play_pause()
    elif action == "next":
        next_track()
    elif action == "prev":
        prev_track()
    elif action == "stop":
        stop()
    return "OK"

@app.route("/volume/up")
def volume_up_route():
    volume_up()
    return "OK"

@app.route("/volume/down")
def volume_down_route():
    volume_down()
    return "OK"

@app.route("/volume/set/<int:level>")
def set_volume_route(level):
    set_system_volume(level / 100.0)
    return "OK"

@app.route("/volume/get")
def get_volume_route():
    return str(get_system_volume())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
