from flask import Flask, render_template, request, send_file
from rembg import remove
from PIL import Image
from io import BytesIO

app = Flask(__name__)

app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024  # 5MB

def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im

def fix_image(upload):
    image = Image.open(upload)
    fixed = remove(image)
    return fixed

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    upload_file = request.files['file']
    if upload_file and upload_file.filename != '':
        if upload_file.content_length > app.config["MAX_CONTENT_LENGTH"]:
            return "The uploaded file is too large. Please upload an image smaller than 5MB.", 400
        else:
            fixed_image = fix_image(upload_file)
            return send_file(BytesIO(convert_image(fixed_image)),
                             download_name="object-img.png",
                             mimetype="image/png")

if __name__ == '__main__':
    app.run(port = 8080)
