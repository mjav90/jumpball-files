from flask import Flask, render_template
import subprocess
import threading

app = Flask(__name__)

def run_game():
    subprocess.Popen(["python", "mygame.py"])  # This runs your game file

@app.route('/')
def index():
    # Start the game when someone visits the page
    threading.Thread(target=run_game, daemon=True).start()
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
