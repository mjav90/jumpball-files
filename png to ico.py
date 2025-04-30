from PIL import Image

img = Image.open("images/ball_prev_ui.png")
img.save("images/ball_prev_ui.ico", format="ICO")
