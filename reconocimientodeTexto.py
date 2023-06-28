from flask import Flask, render_template, request
import pytesseract
from PIL import Image
import re
from collections import Counter

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    image = request.files['image']

    img = Image.open(image)
    text = pytesseract.image_to_string(img)

    line_count = count_lines(text)
    top_words = get_top_words(text)

    return render_template('result.html', text=text, line_count=line_count, top_words=top_words)

def count_lines(text):
    lines = text.strip().split('\n')
    return len(lines)

def get_top_words(text, n=5):
    words = re.findall(r'\b\w+\b', text.lower())
    word_count = Counter(words)
    top_words = word_count.most_common(n)
    return top_words

if __name__ == '__main__':
    app.run(debug=True)
