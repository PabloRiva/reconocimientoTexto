from flask import Flask, render_template, request
import pytesseract
from PIL import Image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    image = request.files['image']
    
    img = Image.open(image)
    text = pytesseract.image_to_string(img)

    return render_template('result.html', text=text)

if __name__ == '__main__':
    app.run(debug=True)
