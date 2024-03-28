from flask import Flask, render_template, request
from rembg import remove
from PIL import Image
from io import BytesIO
import base64

app = Flask(__name__)

app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024  # 5MB

def fix_image(upload):
    image = Image.open(upload)
    fixed = remove(image)
    return fixed

def convert_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return img_str

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
            converted_image_base64 = convert_to_base64(fixed_image)
            return render_template('index.html', converted_image=converted_image_base64)

if __name__ == '__main__':
    app.run()
