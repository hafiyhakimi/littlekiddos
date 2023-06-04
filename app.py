from flask import Flask, render_template, request

app = Flask(__name__, static_folder= 'assets')

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/result', methods=['POST'])
def result():
    input_text = request.form['text']
    image_kid = get_image_kid(input_text)
    image_parent = get_image_parent(input_text)
    name_kid = get_name_kid(input_text)
    return render_template('result.html', image_kid=image_kid, image_parent=image_parent, name_kid=name_kid)

def get_image_kid(input_text):
    # Replace this with your logic to map input text to image filenames
    # Example mapping for demo purposes
    image_mapping = {
        'hanna': 'hanna.jpg',
        'encem': 'encem.jpg'
    }
    return image_mapping.get(input_text)

def get_image_parent(input_text):
    # Replace this with your logic to map input text to image filenames
    # Example mapping for demo purposes
    image_mapping = {
        'hanna': 'encem.jpg',
        'encem': 'encem.jpg'
    }
    return image_mapping.get(input_text)

def get_name_kid(input_text):
    # Replace this with your logic to map input text to image filenames
    # Example mapping for demo purposes
    image_mapping = {
        'hanna': 'Hanna Mardhiah',
        'encem': 'encem.jpg'
    }
    return image_mapping.get(input_text)

if __name__ == '__main__':
    app.run()
