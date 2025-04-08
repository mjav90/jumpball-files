from flask import Flask, Response, render_template_string
import jumpball  # Import your separate pygame file

app = Flask(__name__)

@app.route("/")
def index():
    """Main page."""
    return render_template_string("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Game Stream</title>
        </head>
        <body>
            <h1>Game Stream</h1>
            <img id="game" src="/video_feed" style="width:400px;height:300px;">
        </body>
        </html>
    """)

@app.route('/video_feed')
def video_feed():
    """Stream the frames from the Pygame module."""
    def generate():
        while True:
            frame = pygame_module.get_frame()  # Fetch a frame from the Pygame file
            yield (b'--frame\r\n'
                   b'Content-Type: image/png\r\n\r\n' + frame + b'\r\n')

    return Response(generate(), content_type='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True, threaded=True)